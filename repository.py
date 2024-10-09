from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017')
db = client['BookDatabase']

class Repository:
    def __init__(self, collection_name):
        self.collection = db[collection_name]

    def find_all(self):
        return list(self.collection.find())

    def find_by_id(self, id):
        return self.collection.find_one({'_id': id})

    def create(self, data):
        # Add a '_id' field to leverage ObjectId's timestamp for creation time
        data['_id'] = self.collection.insert_one(data).inserted_id
        return data['_id']

    def update(self, id, data):
        # Set the 'updated_at' field to the current time
        data['updated_at'] = datetime.now()
        result = self.collection.replace_one({'_id': id}, data)
        return result.modified_count > 0

    def delete(self, id):
        result = self.collection.delete_one({'_id': id})
        return result.deleted_count > 0
