from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
import logging
from bson import json_util
import json

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    client = MongoClient('mongodb://mongo-service:27017/')
    db = client['fastapi']
    hits_collection = db['hits']
    logger.info("Successfully connected to MongoDB")
except Exception as e:
    logger.error(f"Could not connect to MongoDB: {e}")

@app.get("/")
def read_root():
    try:
        result = hits_collection.update_one(
            {'_id': 'counter'},
            {'$inc': {'value': 1}},
            upsert=True
        )
        hits = hits_collection.find_one({'_id': 'counter'})
        return {
            "message": "Message: Success",
            "hits": hits['value'] if hits else 0
        }
    except Exception as e:
        logger.error(f"MongoDB error: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to MongoDB")

@app.get("/test")
def read_simple():
    return {"message": "This is a simple response"}