# 🎬 Movie Semantic Search Assignment  

This repository contains my solution for the **Semantic Search on Movie Plots Assignment**.  
The goal was to build a semantic search engine that retrieves movies based on the *meaning* of a query instead of just keyword matches.  

The project uses **SentenceTransformers (all-MiniLM-L6-v2)** for embeddings and **cosine similarity** for ranking results.  
All work was completed step by step as per the assignment instructions, tested with unit tests, and verified using **GitHub Actions CI/CD**.  

---

## 📑 Table of Contents  

1. [Project Overview](#-project-overview)  
2. [Features](#-features)  
3. [Setup Instructions](#-setup-instructions)  
4. [Usage Example](#-usage-example)  
5. [Testing](#-testing)  
6. [Continuous Integration (GitHub Actions)](#-continuous-integration-github-actions)  
7. [Repository Structure](#-repository-structure)  
8. [Step-by-Step Assignment Journey](#-step-by-step-assignment-journey)  
9. [Learnings & Reflections](#-learnings--reflections)  
10. [Future Improvements](#-future-improvements)  
11. [Author](#-author)  

---

## 🎯 Project Overview  

- **Objective**: Implement a semantic search engine for movie plots.  
- **Model Used**: SentenceTransformers → `all-MiniLM-L6-v2`.  
- **Similarity Measure**: Cosine similarity on embeddings.  
- **Evaluation**: Verified with unit tests (`tests/test_movie_search.py`).  
- **Automation**: Continuous testing with GitHub Actions.  

This project demonstrates NLP, embeddings, semantic retrieval, unit testing, and GitHub workflows.  

---

## ✨ Features  

- Load `movies.csv` dataset into Pandas.  
- Generate embeddings for each movie plot.  
- Implement `search_movies(query, top_n)` to return top matches.  
- All **4 unit tests** passing:
  - Output format  
  - Top N correctness  
  - Similarity ranking  
  - Semantic relevance  
- GitHub Actions workflow for automated testing.  

---

## 📦 Setup Instructions  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/movie-search-assignment_221020444.git
   cd movie-search-assignment_221020444



Test Cases Passes proof:
<img width="1388" height="324" alt="image" src="https://github.com/user-attachments/assets/b7ef92b2-2117-4335-a8d8-5886308b8ee0" />
