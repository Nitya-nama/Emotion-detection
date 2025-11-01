from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from transformers import pipeline
import os

app = Flask(__name__)

# ==========================================
# 🔗 MongoDB Atlas Connection (Cloud)
# ==========================================
# Replace <username> and <password> with your Atlas credentials
MONGO_URI = "your-mongodb-atlas-uri"
try:
    client = MongoClient(MONGO_URI)
    db = client["emotion_game"]         # Database name
    collection = db["predictions"]      # Collection name
    print("✅ Connected to MongoDB Atlas successfully!")
except Exception as e:
    print("❌ MongoDB Atlas connection failed:", e)


# ==========================================
# 🧠 Hugging Face Emotion Model
# ==========================================
print("⏳ Loading emotion model (this may take a few seconds)...")
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)
print("✅ Emotion model loaded successfully!")


def get_emotion(text):
    """Predict emotion using Hugging Face model"""
    result = emotion_model(text)[0]
    label = result['label'].capitalize()
    score = result['score']
    return f"{label} ({score:.2f})"


# ==========================================
# 🌐 Flask Routes
# ==========================================
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_text = data.get('text', '')

    if not user_text.strip():
        return jsonify({"error": "Please enter a sentence!"}), 400

    # Predict emotion using Hugging Face model
    emotion = get_emotion(user_text)

    # Save result to MongoDB Atlas
    try:
        collection.insert_one({
            "text": user_text,
            "emotion": emotion,
            "timestamp": datetime.now()
        })
        print(f"✅ Saved to MongoDB Atlas → {emotion}")
    except Exception as e:
        print("⚠️ Could not save to MongoDB Atlas:", e)

    return jsonify({"emotion": emotion})

@app.route('/history')
def history():
    """Show all past detected emotions + chart"""
    data = list(collection.find({}, {"_id": 0, "text": 1, "emotion": 1, "timestamp": 1}))
    return render_template('history.html', records=data)


# ==========================================
# 🚀 Run Flask App
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)

