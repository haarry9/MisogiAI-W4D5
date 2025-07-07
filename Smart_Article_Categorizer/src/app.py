from flask import Flask, request, jsonify, render_template
import numpy as np

# Import our dummy modules
from . import embeddings
from . import classifier

# Initialize the Flask app
app = Flask(__name__, template_folder='../templates')

# --- Model Loading ---
# In a real app, you'd load these properly. For now, we use dummy loaders.
print("Loading models and classifiers at startup...")
classifier.load_classifiers()
w2v_model = embeddings.load_dummy_model("Word2Vec")
sbert_model = embeddings.load_dummy_model("Sentence-BERT")
# BERT and OpenAI models would be loaded here too if they had state.
print("Startup loading complete.")
# --- End Model Loading ---

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify_article():
    """
    The main classification endpoint.
    Takes article text and returns classifications from all models.
    """
    data = request.get_json()
    article_text = data.get('article_text', '')

    if not article_text.strip():
        return jsonify({"error": "Article text cannot be empty."}), 400

    results = {}

    # 1. Word2Vec
    w2v_emb = embeddings.get_word2vec_embedding(article_text, w2v_model)
    category, score = classifier.classify_with_model(w2v_emb, 'Word2Vec')
    results['Word2Vec'] = {'category': category, 'confidence': f"{score:.2f}"}

    # 2. BERT
    bert_emb = embeddings.get_bert_embedding(article_text, None, None)
    category, score = classifier.classify_with_model(bert_emb, 'BERT')
    results['BERT'] = {'category': category, 'confidence': f"{score:.2f}"}

    # 3. Sentence-BERT
    sbert_emb = embeddings.get_sentence_bert_embedding(article_text, sbert_model)
    category, score = classifier.classify_with_model(sbert_emb, 'Sentence-BERT')
    results['Sentence-BERT'] = {'category': category, 'confidence': f"{score:.2f}"}

    # 4. OpenAI
    openai_emb = embeddings.get_openai_embedding(article_text, None)
    category, score = classifier.classify_with_model(openai_emb, 'OpenAI')
    results['OpenAI'] = {'category': category, 'confidence': f"{score:.2f}"}

    return jsonify(results)

if __name__ == '__main__':
    # Note: Using `debug=True` is not recommended for production.
    app.run(debug=True, port=5000) 