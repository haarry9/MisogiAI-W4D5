import os
from src.data_preprocessing import load_data
from src.fine_tune import fine_tune_embeddings
from src.predict import train_prediction_model, predict_conversion
from src.evaluate import evaluate_model

def main():
    """
    Main function to run the entire pipeline.
    """
    print("--- Starting Sales Conversion Prediction Pipeline ---")

    # Create models directory if it doesn't exist
    if not os.path.exists("models"):
        os.makedirs("models")

    # 1. Load and preprocess data
    print("\nStep 1: Loading data...")
    data = load_data('data/dummy_sales_calls.csv')
    if data is None:
        print("Failed to load data. Exiting.")
        return

    # 2. Fine-tune embeddings
    print("\nStep 2: Fine-tuning embeddings (simulation)...")
    model_path = fine_tune_embeddings(data)

    # 3. Train prediction model
    print("\nStep 3: Training prediction model...")
    classifier_path = train_prediction_model(data, model_path)

    # 4. Evaluate the model
    print("\nStep 4: Evaluating the model...")
    evaluate_model(data, model_path, classifier_path)

    # 5. Run a prediction on new, unseen data
    print("\nStep 5: Running prediction on new examples...")
    new_transcripts = [
        "This sounds interesting, tell me more about the pricing.",
        "Not interested, thank you."
    ]
    predictions = predict_conversion(new_transcripts, model_path, classifier_path)

    if predictions is not None:
        print("\n--- Example Predictions ---")
        for transcript, prob in zip(new_transcripts, predictions):
            print(f"Transcript: '{transcript}'")
            print(f"  -> Predicted Conversion Probability: {prob:.4f}")
        print("---------------------------\n")

    print("--- Pipeline Finished ---")

if __name__ == '__main__':
    main() 