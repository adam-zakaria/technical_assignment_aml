import time
from pymongo import MongoClient

def reindex_collection(database_name, collection_name):
    # Create a MongoClient to the running mongod instance
    client = MongoClient('mongodb://localhost:27017/')
    
    # Get a reference to your database
    db = client[database_name]

    # Get a reference to your collection
    collection = db[collection_name]

    # Reindex the collection
    collection.reIndex()

if __name__ == "__main__":
    while True:
        reindex_collection('test_database', 'test_collection')
        # Sleep for 7 days (60 seconds/minute, 60 minutes/hour, 24 hours/day, 7 days)
        time.sleep(60 * 60 * 24 * 7)
