# Intelligent Document Chunking for Enterprise Knowledge Management

This project implements an adaptive chunking system designed to improve knowledge retrieval from diverse enterprise document repositories. By intelligently classifying documents and applying tailored chunking strategies, the system enhances the accuracy and relevance of information retrieval for internal teams and support automation.

## Problem Statement

In large enterprise knowledge bases, content varies widely from technical documentation and API references to support tickets and internal policies. A one-size-fits-all chunking approach often fails to preserve the contextual integrity of these documents. For example, code snippets may be fragmented, troubleshooting steps separated, and policy requirements disconnected, leading to poor retrieval accuracy and inefficient knowledge access.

## Solution

This system addresses the challenge by implementing a multi-stage pipeline:

1.  **Document Classification**: Automatically detects the type of content (e.g., technical doc, support ticket, API reference, policy) based on its structure and content patterns.

2.  **Adaptive Chunking**: Applies a document-specific chunking strategy to preserve context:
    *   **Semantic Chunking**: For narrative-heavy documents like policies and tutorials.
    *   **Code-Aware Chunking**: For technical documents and API references containing code snippets.
    *   **Hierarchical Chunking**: For structured documents, maintaining their inherent hierarchy.

3.  **LangChain Integration**: Orchestrates the entire processing pipeline, from document ingestion to updating the vector store with optimally chunked content.

4.  **Performance Monitoring**: Includes mechanisms to track retrieval accuracy and other key performance indicators, allowing for continuous refinement of chunking strategies.

## Project Structure
```
.
├── data
│   └── samples
│       ├── sample_api_doc.py
│       ├── sample_policy.txt
│       └── sample_ticket.md
├── src
│   ├── chunking_strategies
│   │   ├── __init__.py
│   │   ├── code_chunker.py
│   │   ├── hierarchical_chunker.py
│   │   └── semantic_chunker.py
│   ├── document_classification
│   │   ├── __init__.py
│   │   └── classifier.py
│   ├── monitoring
│   │   ├── __init__.py
│   │   └── performance.py
│   ├── pipeline
│   │   ├── __init__.py
│   │   └── orchestrator.py
│   └── main.py
├── README.md
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.8+
- Pip

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the document processing pipeline, execute the main script:

```bash
python src/main.py
```

This will process the sample documents located in the `data/samples` directory, classify them, apply the appropriate chunking strategy, and simulate updating a vector store.

## Key Components

### Document Classification

The `src/document_classification/classifier.py` module contains the logic for identifying document types. It uses a model to analyze text and structural patterns.

### Chunking Strategies

The `src/chunking_strategies/` directory houses the different chunking algorithms:
- `code_chunker.py`: Handles syntax-aware splitting of code.
- `semantic_chunker.py`: Splits text based on semantic meaning and context.
- `hierarchical_chunker.py`: Preserves the structure of documents like FAQs or guides.

### Pipeline Orchestration

The `src/pipeline/orchestrator.py` module, powered by LangChain, manages the end-to-end workflow, ensuring seamless integration of all components.

### Performance Monitoring

The `src/monitoring/performance.py` module provides tools to evaluate retrieval accuracy and processing efficiency, offering insights for ongoing system optimization. 