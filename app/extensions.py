from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["github"]
collection = db["events"]

def get_collection():
    return collection