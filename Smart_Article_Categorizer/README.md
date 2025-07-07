# Smart Article Categorizer

A system that automatically classifies articles into 6 categories (Tech, Finance, Healthcare, Sports, Politics, Entertainment) using different embedding approaches.

## Project Overview

This project implements and compares four different text embedding models for news article classification. A simple web UI is provided for real-time classification and model comparison.

### Categories
1.  Tech
2.  Finance
3.  Healthcare
4.  Sports
5.  Politics
6.  Entertainment

### Embedding Models Implemented
1.  **Word2Vec/GloVe**: Average word vectors for document representation.
2.  **BERT**: Uses `[CLS]` token embeddings for sentence-level meaning.
3.  **Sentence-BERT**: Generates direct sentence embeddings using `all-MiniLM-L6-v2`.
4.  **OpenAI**: Leverages the `text-embedding-ada-002` API for powerful embeddings.

## Technical Stack
-   **Backend**: Python, Flask, Scikit-learn
-   **Frontend**: HTML, CSS, JavaScript
-   **ML/NLP**: Transformers, Sentence-Transformers, OpenAI, Gensim

## Getting Started

### Prerequisites
-   Python 3.8+
-   Conda or venv

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd Smart_Article_Categorizer
    ```

2.  **Set up the environment and install dependencies:**
    ```bash
    # Using conda
    conda create --name smart-categorizer python=3.9
    conda activate smart-categorizer

    pip install -r requirements.txt
    ```

3.  **Set up your OpenAI API Key:**
    Create a `.env` file in the root directory and add your key:
    ```
    OPENAI_API_KEY="your-key-here"
    ```

### Running the Application

To start the web server, run:
```bash
python src/app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure
```
.
├── src/
│   ├── __init__.py
│   ├── app.py              # Flask web server
│   ├── classifier.py       # Classification logic
│   └── embeddings.py       # Embedding model implementations
├── templates/
│   └── index.html          # Frontend UI
├── .env                    # For API keys
├── .gitignore
└── requirements.txt        # Python dependencies
``` 