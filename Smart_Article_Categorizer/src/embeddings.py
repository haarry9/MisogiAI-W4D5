import numpy as np

# Dummy data and models
def load_dummy_model(model_type):
    """A dummy function to simulate loading a model."""
    print(f"Loading dummy {model_type} model...")
    # Return a dummy object that mimics a model
    class DummyModel:
        def __init__(self):
            self.vector_size = 100 # Example vector size

        def wv(self, word):
            return np.random.rand(self.vector_size)

        def encode(self, text):
            return np.random.rand(384) # For Sentence-BERT
            
    return DummyModel()

def get_word2vec_embedding(text, model):
    """Generates a dummy Word2Vec embedding by averaging word vectors."""
    print("Generating Word2Vec embedding...")
    words = text.split()
    if not words:
        return np.zeros(model.vector_size)
    
    vectors = [model.wv(word) for word in words if word in model.wv]
    if not vectors:
        return np.zeros(model.vector_size)
        
    return np.mean(vectors, axis=0)

def get_bert_embedding(text, model, tokenizer):
    """Generates a dummy BERT [CLS] token embedding."""
    print("Generating BERT embedding...")
    # In a real scenario, you would tokenize and get the [CLS] token's embedding
    return np.random.rand(768) # Typical BERT base model embedding size

def get_sentence_bert_embedding(text, model):
    """Generates a dummy Sentence-BERT embedding."""
    print("Generating Sentence-BERT embedding...")
    return model.encode(text)

def get_openai_embedding(text, client):
    """Generates a dummy OpenAI embedding."""
    print("Generating OpenAI embedding...")
    # In a real scenario, you would call the OpenAI API
    return np.random.rand(1536) # OpenAI ada-002 embedding size

if __name__ == '__main__':
    # Example usage (for testing purposes)
    sample_text = "This is a test article about technology and finance."

    # Dummy Word2Vec
    w2v_model = load_dummy_model("Word2Vec")
    w2v_emb = get_word2vec_embedding(sample_text, w2v_model)
    print(f"Word2Vec Embedding shape: {w2v_emb.shape}")

    # Dummy BERT (model and tokenizer would be loaded from transformers)
    bert_emb = get_bert_embedding(sample_text, None, None)
    print(f"BERT Embedding shape: {bert_emb.shape}")
    
    # Dummy Sentence-BERT
    sbert_model = load_dummy_model("Sentence-BERT")
    sbert_emb = get_sentence_bert_embedding(sample_text, sbert_model)
    print(f"Sentence-BERT Embedding shape: {sbert_emb.shape}")

    # Dummy OpenAI (client would be initialized)
    openai_emb = get_openai_embedding(sample_text, None)
    print(f"OpenAI Embedding shape: {openai_emb.shape}") 