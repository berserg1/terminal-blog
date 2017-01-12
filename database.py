import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"  # Static variables shared between all Database class instances
    DATABASE = None

    @staticmethod  # This means that a method doesn't take any obligatory params (like self)
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['udemypyweb']

    @staticmethod
    def insert(collection, data):  # Insert document into a collection
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):  # Find documents in a collection, returns pymongo Cursor object
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):  # Find a document in a collection (json object)
        return Database.DATABASE[collection].find_one(query)
