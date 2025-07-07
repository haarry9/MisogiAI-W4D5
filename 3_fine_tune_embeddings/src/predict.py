from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

def train_prediction_model(data, model_path):
    """
    Train a simple classifier on top of the embeddings.
    """
    print("Training prediction model...")
    model = SentenceTransformer(model_path)
    
    embeddings = model.encode(data['transcript'].tolist())
    
    X_train, X_test, y_train, y_test = train_test_split(
        embeddings, data['conversion'], test_size=0.2, random_state=42
    )
    
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    
    print("Prediction model training complete.")
    
    classifier_path = "./models/prediction_classifier.joblib"
    joblib.dump(classifier, classifier_path)
    print(f"Classifier saved to {classifier_path}")
    
    return classifier_path

def predict_conversion(transcripts, model_path, classifier_path):
    """
    Predicts conversion probability for a list of transcripts.
    """
    print("Making predictions...")
    if not os.path.exists(model_path) or not os.path.exists(classifier_path):
        print("Error: Model or classifier not found. Please run fine-tuning and training first.")
        return None
        
    model = SentenceTransformer(model_path)
    classifier = joblib.load(classifier_path)
    
    embeddings = model.encode(transcripts)
    
    probabilities = classifier.predict_proba(embeddings)
    
    # Return probability of positive class (conversion=1)
    return probabilities[:, 1]

if __name__ == '__main__':
    # Example of how to use this module
    from data_preprocessing import load_data
    
    data = load_data('data/dummy_sales_calls.csv')
    if data is not None:
        model_path = "./models/fine_tuned_model"
        if not os.path.exists(model_path):
            print("Fine-tuned model not found. Running a dummy fine-tuning process.")
            from fine_tune import fine_tune_embeddings
            if not os.path.exists("./models"):
                os.makedirs("./models")
            fine_tune_embeddings(data)

        classifier_path = train_prediction_model(data, model_path)

        new_transcripts = [
            "Hello, I'd like to ask about your services.",
            "I am not interested, please remove me from your list."
        ]
        
        predictions = predict_conversion(new_transcripts, model_path, classifier_path)
        
        if predictions is not None:
            print("\nPredictions for new transcripts:")
            for transcript, prob in zip(new_transcripts, predictions):
                print(f"Transcript: '{transcript}' -> Conversion Probability: {prob:.4f}") 