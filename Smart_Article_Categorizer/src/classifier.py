import numpy as np
from sklearn.linear_model import LogisticRegression
import random

# Dummy pre-trained classifiers
DUMMY_CLASSIFIERS = {}
CATEGORIES = ['Tech', 'Finance', 'Healthcare', 'Sports', 'Politics', 'Entertainment']

def train_dummy_classifier(embedding_name):
    """
    Simulates training a Logistic Regression classifier.
    In a real scenario, this would take embeddings and labels.
    """
    print(f"Training dummy classifier for {embedding_name}...")
    # Create a dummy classifier, "trained" on random data
    clf = LogisticRegression()
    # Fit with random data to make it a "fitted" model
    dummy_features = np.random.rand(10, 100)
    dummy_labels = np.random.randint(0, len(CATEGORIES), 10)
    clf.fit(dummy_features, dummy_labels)
    return clf

def load_classifiers():
    """Loads or 'trains' all dummy classifiers."""
    global DUMMY_CLASSIFIERS
    embedding_models = ['Word2Vec', 'BERT', 'Sentence-BERT', 'OpenAI']
    for model_name in embedding_models:
        DUMMY_CLASSIFIERS[model_name] = train_dummy_classifier(model_name)
    print("All dummy classifiers are loaded.")

def classify_with_model(embedding, model_name):
    """
    Classifies a given embedding using a pre-trained dummy model.
    Returns a predicted category and a dummy confidence score.
    """
    if model_name not in DUMMY_CLASSIFIERS:
        raise ValueError(f"Classifier for {model_name} not found.")
    
    # In a real classifier, you'd predict based on the actual embedding.
    # Here, we just return a random prediction for demonstration.
    predicted_category = random.choice(CATEGORIES)
    confidence_score = random.uniform(0.6, 0.99)
    
    print(f"Model {model_name} predicts: {predicted_category} with confidence {confidence_score:.2f}")
    
    return predicted_category, confidence_score

if __name__ == '__main__':
    # Initialize the classifiers when run as a script
    load_classifiers()

    # Create a dummy embedding to test classification
    dummy_embedding = np.random.rand(1, 100) # Shape must match training data for a real model

    # Test classification for each model type
    for name in DUMMY_CLASSIFIERS.keys():
        category, score = classify_with_model(dummy_embedding, name)
        # Note: The dummy embedding won't match every model's expected input size,
        # but our dummy `classify_with_model` function ignores the input anyway. 