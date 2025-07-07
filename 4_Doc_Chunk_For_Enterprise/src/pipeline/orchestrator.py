from src.document_classification.classifier import DocumentClassifier
from src.chunking_strategies.code_chunker import CodeChunker
from src.chunking_strategies.semantic_chunker import SemanticChunker
from src.chunking_strategies.hierarchical_chunker import HierarchicalChunker

class PipelineOrchestrator:
    """
    Orchestrates the entire document processing pipeline, from classification
    to chunking and vector store updates.
    """
    def __init__(self):
        """
        Initializes the orchestrator and its components.
        """
        self.classifier = DocumentClassifier()
        self.chunkers = {
            "api_reference": CodeChunker(),
            "technical_doc": SemanticChunker(),
            "support_ticket": HierarchicalChunker(),
            "policy": SemanticChunker(),
            "tutorial": HierarchicalChunker(),
        }
        # In a real system, this would be a connection to a vector database.
        self.vector_store = []
        print("Initialized Pipeline Orchestrator.")

    def process_document(self, file_path: str, content: str):
        """
        Processes a single document.

        Args:
            file_path (str): The path to the document.
            content (str): The content of the document.
        """
        print(f"\\n--- Processing document: {file_path} ---")
        
        # 1. Classify the document
        doc_type = self.classifier.classify(content)
        print(f"Document classified as: {doc_type}")

        # 2. Select and apply the appropriate chunker
        chunker = self.chunkers.get(doc_type)
        if not chunker:
            print(f"No chunker found for type '{doc_type}', using default semantic chunker.")
            chunker = SemanticChunker()
        
        chunks = chunker.chunk(content)
        
        # 3. Simulate updating the vector store
        self._update_vector_store(chunks, file_path)
        
        print(f"--- Finished processing {file_path} ---")

    def _update_vector_store(self, chunks: list, source: str):
        """
        Simulates adding chunks to a vector store.
        """
        # In a real implementation, this would involve creating embeddings
        # and upserting them into a vector database like ChromaDB or Pinecone.
        for i, chunk in enumerate(chunks):
            self.vector_store.append({
                "id": f"{source}-{i}",
                "content": chunk,
                "source": source,
            })
        print(f"Updated vector store with {len(chunks)} chunks from {source}.")

    def get_vector_store_size(self) -> int:
        return len(self.vector_store) 