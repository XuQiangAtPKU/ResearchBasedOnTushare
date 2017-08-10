from pymongo import MongoClient

class MongoConnection(object):
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/');

    def GetClient(self):
        return self.client;

mongoConnection = MongoConnection();