from pymongo import MongoClient

client = MongoClient("your-mongodb-atlas-uri ")
db = client["emotion_game"]

collection = db["emotions"]
