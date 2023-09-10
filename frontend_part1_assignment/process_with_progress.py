from tqdm import tqdm
from pymongo import MongoClient
import time

client = MongoClient('mongodb://localhost:27017/')
db = client.progress_database
collection = db.progress_collection

def process_with_progress(task_id):
    total = 100
    for i in tqdm(range(total)):
        time.sleep(0.1)  # Simulate some processing time
        progress_percentage = (i + 1) * 100 / total
        collection.update_one({'task_id': task_id}, {'$set': {'progress': progress_percentage}}, upsert=True)

if __name__ == "__main__":
    task_id = 'task_1'
    process_with_progress(task_id)
