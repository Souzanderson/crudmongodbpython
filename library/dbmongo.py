from pymongo import MongoClient
import pymongo

class DbMongo():
    def __init__(self, location, banco, port = 27017):
        # print(f"[CONNECT MONGODB] >> location: {location} >> db: {banco} >> port: {port}")
        self.client = MongoClient(location, port)
        self.db = self.client[banco]
        
    def getDb(self):
        return self.db
        
    def insert(self,table,value):
        try:
            collection = self.db[table]
            collection.insert_one(value)
            return True
        except Exception as e:
            print(e)
            return False
        
    def insert_or_update(self,table, idvalue, value):
        try:
            value["_id"] = idvalue
            res = self.update_one(table, idvalue, value)
            if not res:
                self.insert(table, value)
            return True
        except Exception as e:
            return None
    
    def insert_list(self, table, listvalues):
        try:
            if(isinstance(listvalues,dict)):
                return self.insert(table,listvalues)
            collection = self.db[table]
            _ids = collection.insert_many(listvalues).inserted_ids
            return _ids
        except Exception as e:
            return []
    
    def select_one(self, table, query, columns=None):
        try:
            collection = self.db[table]
            if columns:
                values = collection.find_one(query,columns)
            else:
                values = collection.find_one(query)
            return values
        except Exception as e:
            return {}
        
    def select(self, table, query={}, columns=None, orderby=None, direction = pymongo.DESCENDING, limit=None):
        try:
            collection = self.db[table]
            if not columns:
                c = collection.find(query)
            else:
                c = collection.find(query, columns)
            if orderby:
                c = c.sort(orderby, direction)
            if limit:
                c = c.limit(limit)
            return [doc for doc in c]
        except Exception as e:
            return None
    
    def update_one(self, table, id, value):
        try:
            collection = self.db[table]
            res = collection.replace_one({"_id": id}, value)
            return res.raw_result.get('updatedExisting')
        except Exception as e:
            return False
    
    def update_by_id(self, table, id, values):
        try:
            collection = self.db[table]
            _id = collection.update_one({"_id":id},{"$set": values})
            return _id
        except Exception as e:
            print(e)
            return None
    
    def delete(self,table, condition):
        try:
            collection = self.db[table]
            collection.delete_many(condition)
        except Exception as e:
            print(e)
    
    def tables(self):
        try:
            return self.db.list_collection_names()
        except Exception as e:
            return None