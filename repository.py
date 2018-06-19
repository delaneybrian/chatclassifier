import pymongo
from pymongo import MongoClient
from bson.json_util import dumps

class Repository:

    def __init__(self):
        self.client = MongoClient("mongodb://chatclassifieradmin:twilightstruggle1960@ds016128.mlab.com:16128/chatclassifier")
        self.db = self.client['chatclassifier']

    def getChatById(self, id):
        chatCollection = self.db["testcollection"]
        bsonChat = chatCollection.find_one({"name": "ladsChat"})
        jsonChat = dumps(bsonChat)
        return jsonChat
