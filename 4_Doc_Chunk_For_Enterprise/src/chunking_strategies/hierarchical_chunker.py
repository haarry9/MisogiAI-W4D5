from typing import List, Dict, Any

class HierarchicalChunker:
    """
    A chunker that understands the structure of a document,
    such as sections and subsections.
    """
    def __init__(self, levels: List[str] = None):
        """
        Initializes the hierarchical chunker.

        Args:
            levels (List[str]): The hierarchical levels to look for (e.g., ['h1', 'h2', 'h3']).
        """
        self.levels = levels or ['#', '##', '###']
        print("Initialized Hierarchical Chunker.")

    def chunk(self, document_content: str) -> List[Dict[str, Any]]:
        """
        Chunks the document based on its hierarchical structure.

        Args:
            document_content (str): The content of the document (e.g., Markdown).

        Returns:
            List[Dict[str, Any]]: A list of chunks, each with content and metadata.
        """
        # This is a simplified logic for demonstration.
        # It splits the document by Markdown headers.
        chunks = []
        lines = document_content.split('\\n')
        current_chunk = {'content': '', 'metadata': {}}
        
        for line in lines:
            is_header = False
            for i, level in enumerate(self.levels):
                if line.strip().startswith(level):
                    if current_chunk['content']:
                        chunks.append(current_chunk)
                    
                    current_chunk = {
                        'content': line.strip(),
                        'metadata': {'level': i + 1, 'header': line.strip().lstrip(level).strip()}
                    }
                    is_header = True
                    break
            
            if not is_header:
                current_chunk['content'] += '\\n' + line

        if current_chunk['content']:
            chunks.append(current_chunk)
            
        print(f"Document hierarchically chunked into {len(chunks)} parts.")
        return chunks 