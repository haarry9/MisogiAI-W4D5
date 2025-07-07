from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sentence_transformers import SentenceTransformer
import joblib
import numpy as np

def evaluate_model(data, model_path, classifier_path):
    """
    Evaluates the performance of the model on the test set.
    """
    print("Evaluating model performance...")
    
    # In a real scenario, you would have a separate test set.
    # Here, we'll just use the same data for simplicity.
    test_data = data
    
    model = SentenceTransformer(model_path)
    classifier = joblib.load(classifier_path)
    
    embeddings = model.encode(test_data['transcript'].tolist())
    labels = test_data['conversion']
    
    predictions = classifier.predict(embeddings)
    
    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='binary')
    
    print("\n--- Evaluation Results ---")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")
    print("------------------------\n")
    
    # In a real project, you would also compare this to a generic, non-fine-tuned model.
    print("(Note: For a full evaluation, compare these metrics against a baseline model.)")

if __name__ == '__main__':
    from data_preprocessing import load_data
    from predict import train_prediction_model
    from fine_tune import fine_tune_embeddings
    import os
    
    data = load_data('data/dummy_sales_calls.csv')
    if data is not None:
        model_path = "./models/fine_tuned_model"
        classifier_path = "./models/prediction_classifier.joblib"
        
        if not all(os.path.exists(p) for p in [model_path, classifier_path]):
            print("Models not found. Running dummy training process.")
            if not os.path.exists("./models"):
                os.makedirs("./models")
            model_path = fine_tune_embeddings(data)
            classifier_path = train_prediction_model(data, model_path)
            
        evaluate_model(data, model_path, classifier_path) 