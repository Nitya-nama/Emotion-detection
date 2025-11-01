from pymongo import MongoClient

client = MongoClient("mongodb+srv://flaskuser:flask123@cluster0.xmpclqw.mongodb.net/?appName=Cluster0")
db = client["emotion_game"]
collection = db["emotions"]