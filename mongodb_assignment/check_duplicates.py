from pymongo import MongoClient

def find_duplicates_in_collection(database_name, collection_name, field_name):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[database_name]
    collection = db[collection_name]

    duplicates = collection.aggregate([
        {
            '$group': {
                '_id': {'field': f'${field_name}'}, 
                'uniqueIds': {'$addToSet': '$_id'}, 
                'count': {'$sum': 1}
            }
        }, 
        {
            '$match': {
                'count': {'$gt': 1}
            }
        }
    ])
    
    for doc in duplicates:
        print(f"Duplicate value: {doc['_id']['field']} found {doc['count']} times.")

if __name__ == "__main__":
    find_duplicates_in_collection('test_database', 'test_collection', 'field_name_to_check')
