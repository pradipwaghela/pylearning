from app.extensions import mongo

class BaseDAO():
    def __init__(self, collection):
        self.collection = collection
    
    def find_one(self,query,projection):
        collection = mongo.db[self.collection]
        return collection.find_one(query=query,projection=projection)
    
    def find(self,query,projection):
        collection = mongo.db[self.collection]
        return collection.find(query=query,projection=projection)
    
    def insert_one(self,data):
        collection = mongo.db[self.collection]
        result = collection.insert_one(data)
        return result.acknowledged 

    def insert_many(self,data):
        collection = mongo.db[self.collection]
        result = collection.insert_many(data)
        return result.acknowledged

    def find_and_update(self,query,data):
        collection = mongo.db[self.collection]
        return collection.find_one_and_delete(query,data)

    def update_one(self,query,data,upsert=False):
        collection = mongo.db[self.collection]
        return collection.update_one(query=query,data=data,upsert=upsert)

    def update_many(self,query,data):
        collection = mongo.db[self.collection]
        return collection.update_many(query=query,data=data)

    def delete_one(self,query):
        collection = mongo.db[self.collection]
        return collection.delete_one(query=query)

    def delete_many(self,query):
        collection = mongo.db[self.collection]
        return collection.delete_one(query=query)

    def count(self,query):
        collection = mongo.db[self.collection]
        return collection.countDocuments(query=query) or collection.estimated_document_count()