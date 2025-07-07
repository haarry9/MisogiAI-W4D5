# Indian Legal Document Search System

A web-based system to search and retrieve Indian legal documents, featuring a comparative analysis of four distinct similarity methods. This project aims to identify the most effective approach for legal document retrieval by evaluating Cosine Similarity, Euclidean Distance, Maximal Marginal Relevance (MMR), and a custom Hybrid Similarity metric.

## Problem Statement

Build a search system for Indian legal documents that compares 4 different similarity methods to find the most effective approach for legal document retrieval.

## Features

-   **Document Upload**: Supports uploading legal documents in PDF and Word formats.
-   **Text-Based Search**: Allows users to input text queries to search through the document corpus.
-   **Multi-Method Comparison**: Displays search results from four different similarity algorithms side-by-side for immediate comparison.
    -   Cosine Similarity
    -   Euclidean Distance
    -   Maximal Marginal Relevance (MMR)
    -   Hybrid Similarity (`0.6 × Cosine + 0.4 × Legal_Entity_Match`)
-   **Performance Dashboard**: Visualizes key performance metrics for each search method, including:
    -   **Precision**: The fraction of relevant documents among the retrieved documents.
    -   **Recall**: The fraction of relevant documents that were successfully retrieved.
    -   **Diversity Score**: A measure of the variety in the search results, particularly for evaluating MMR.

## Tech Stack

-   **Backend**: Python
-   **Web Framework**: Streamlit
-   **Core Libraries**: Pandas, NumPy, Scikit-learn, NLTK
-   **Document Processing**: PyPDF2, python-docx

## Project Structure

```
.
├── app
│   └── app.py              # Main Streamlit application
├── data
│   ├── court_judgements.txt
│   ├── gst_act.txt
│   ├── income_tax_act.txt
│   └── property_law.txt
├── requirements.txt
└── README.md
```

## Setup and Run

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_GITHUB_REPO_URL>
    cd 2_Indian_Legal_System_Doc_Search
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app/app.py
    ```

## Performance Analysis & Recommendations (Dummy)

This section would contain the analysis of the results obtained from the comparison framework.

**Cosine Similarity**:
-   **Performance**: High precision for queries with strong keyword overlap. Tends to retrieve documents that are semantically very close to the query.
-   **Recommendation**: Best for specific, well-defined queries where the user knows the exact legal terminology.

**Euclidean Distance**:
-   **Performance**: Offers a different perspective by measuring the geometric distance in the embedding space. Sometimes surfaces documents that are conceptually related but use different terminology.
-   **Recommendation**: Useful as a secondary method to discover related documents that cosine similarity might miss.

**Maximal Marginal Relevance (MMR)**:
-   **Performance**: Significantly higher diversity score compared to other methods. Reduces redundancy in search results by promoting documents that are relevant but dissimilar to already selected documents.
-   **Recommendation**: Ideal for exploratory searches where the user wants a broad overview of a topic without seeing repetitive information.

**Hybrid Similarity**:
-   **Performance**: Shows strong performance by balancing semantic similarity with the presence of specific legal entities. The `Legal_Entity_Match` component helps in prioritizing documents that mention key legal statutes, sections, or case numbers.
-   **Recommendation**: The most promising method for a production-level legal search system due to its balanced approach. The weights (0.6 and 0.4) can be further tuned based on user feedback.

**Overall Conclusion**: The Hybrid Similarity model is recommended as the default search method for its robust and balanced performance. MMR is a valuable alternative for users conducting exploratory research. 