import os
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Model and data paths
MODEL_NAME = "all-MiniLM-L6-v2"
MOVIES_CSV = "movies.csv"
EMB_CACHE = "movie_embeddings.npy"

_model = None
_movies_df = None
_embeddings = None

def _load_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model

def _load_movies():
    global _movies_df
    if _movies_df is None:
        if not os.path.exists(MOVIES_CSV):
            raise FileNotFoundError(f"{MOVIES_CSV} not found.")
        df = pd.read_csv(MOVIES_CSV)
        if "plot" not in df.columns:
            if "description" in df.columns:
                df.rename(columns={"description": "plot"}, inplace=True)
            else:
                raise KeyError("movies.csv must have a 'plot' or 'description' column.")
        df = df[["title", "plot"]].dropna().reset_index(drop=True)
        _movies_df = df
    return _movies_df

def _compute_embeddings(force_recompute=False):
    global _embeddings
    if _embeddings is not None and not force_recompute:
        return _embeddings
    if os.path.exists(EMB_CACHE) and not force_recompute:
        _embeddings = np.load(EMB_CACHE)
        return _embeddings
    model = _load_model()
    df = _load_movies()
    texts = df["plot"].astype(str).tolist()
    _embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    np.save(EMB_CACHE, _embeddings)
    return _embeddings

def search_movies(query, top_n=10):
    """
    Search for top_n movies most similar to the query.
    Returns DataFrame with title, plot, and similarity.
    """
    if not isinstance(query, str) or query.strip() == "":
        raise ValueError("Query must be a non-empty string.")
    if not isinstance(top_n, int) or top_n <= 0:
        raise ValueError("top_n must be a positive integer.")

    df = _load_movies()
    emb = _compute_embeddings()
    model = _load_model()
    q_emb = model.encode([query], convert_to_numpy=True)
    sims = cosine_similarity(q_emb, emb)[0]

    top_idx = np.argsort(sims)[::-1][:top_n]
    results = df.iloc[top_idx].copy()
    results["similarity"] = sims[top_idx]

    return results[["title", "plot", "similarity"]].reset_index(drop=True)
