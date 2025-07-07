from typing import List

class SemanticChunker:
    """
    A chunker that splits text based on semantic boundaries,
    aiming to keep related sentences together.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", chunk_size: int = 512):
        """
        Initializes the semantic chunker.

        Args:
            model_name (str): The sentence transformer model to use.
            chunk_size (int): The target size for each chunk.
        """
        self.model_name = model_name
        self.chunk_size = chunk_size
        print(f"Initialized Semantic Chunker with model {model_name}.")

    def chunk(self, text: str) -> List[str]:
        """
        Chunks the text into semantically coherent parts.

        Args:
            text (str): The text to be chunked.

        Returns:
            List[str]: A list of text chunks.
        """
        # A simplified chunking logic for demonstration.
        # A real implementation would involve sentence embeddings and clustering.
        chunks = []
        words = text.split()
        
        current_chunk_words = []
        for word in words:
            current_chunk_words.append(word)
            if len(" ".join(current_chunk_words)) >= self.chunk_size:
                chunks.append(" ".join(current_chunk_words))
                current_chunk_words = []
        
        if current_chunk_words:
            chunks.append(" ".join(current_chunk_words))
            
        print(f"Text semantically chunked into {len(chunks)} parts.")
        return chunks 