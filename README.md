# 🎬 Movie Semantic Search Assignment  

This repository contains my solution for **Assignment-1: Semantic Search on Movie Plots**.  
The goal is to build a **semantic search engine** that retrieves movies based on the meaning of a user’s query, not just keyword matching.  

The project uses **SentenceTransformers (all-MiniLM-L6-v2)** for embeddings, **cosine similarity** for comparison, and is verified with **unit tests + GitHub Actions**.  

---

## ✨ Features  

- 📖 Loads movie plots from `movies.csv` into a Pandas DataFrame  
- 🤖 Creates embeddings using **all-MiniLM-L6-v2** from `sentence-transformers`  
- 🔍 Implements a function `search_movies(query, top_n)` to find the most relevant movies  
- ✅ Verified using **unit tests** (`tests/test_movie_search.py`)  
- ⚙️ Continuous Integration (CI) with **GitHub Actions** ensures correctness  

---

## 📦 Setup Instructions  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/movie-search-assignment.git
   cd movie-search-assignment
