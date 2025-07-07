import random

class DocumentClassifier:
    """
    A simple classifier to determine the type of a document.
    """
    def __init__(self):
        """
        Initializes the document classifier.
        In a real implementation, this would load a pre-trained model.
        """
        self._document_types = ["technical_doc", "support_ticket", "api_reference", "policy", "tutorial"]
        print("Initialized Document Classifier.")

    def classify(self, document_content: str) -> str:
        """
        Classifies the document into one of the predefined types.

        Args:
            document_content (str): The text content of the document.

        Returns:
            str: The predicted document type.
        """
        # This is a simplified logic for demonstration purposes.
        if "api" in document_content.lower() or "def" in document_content or "class" in document_content:
            return "api_reference"
        if "ticket" in document_content.lower() or "issue" in document_content.lower():
            return "support_ticket"
        if "policy" in document_content.lower() or "confidential" in document_content.lower():
            return "policy"
        
        # Fallback to a random choice for variety.
        return random.choice(self._document_types)

    def batch_classify(self, documents: list[str]) -> list[str]:
        """
        Classifies a batch of documents.

        Args:
            documents (list[str]): A list of document contents.

        Returns:
            list[str]: A list of predicted document types.
        """
        return [self.classify(doc) for doc in documents] 