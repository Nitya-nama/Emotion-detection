from transformers import pipeline

# Load a pretrained emotion classification model
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)

def get_emotion(text):
    if not text.strip():
        return "Neutral"
    result = emotion_model(text)[0]
    return result['label']
