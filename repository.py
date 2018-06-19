from pymongo import MongoClient
from bson.json_util import dumps
import json

class Repository:

    testCollection = "testcollection"
    scriptCollection = "movietestcollection"
    trainedChatCollection = "testtrainedchatcollection"

    def __init__(self):
        self.client = MongoClient("mongodb://chatclassifieradmin:twilightstruggle1960@ds016128.mlab.com:16128/chatclassifier")
        self.db = self.client['chatclassifier']

    def getChatById(self, id):
        chatCollection = self.db[self.testCollection]
        bsonChat = chatCollection.find_one({"_id": id})
        jsonChat = dumps(bsonChat)
        return jsonChat

    def getScriptById(self, id):
        scriptCollection = self.db[self.scriptCollection]
        bsonScript = scriptCollection.find_one({"_id": id})
        jsonScript = dumps(bsonScript)
        return jsonScript

    def getAllScripts(self, id):
        scriptCollection = self.db[self.scriptCollection]
        bsonScripts = scriptCollection.find()
        jsonScripts = dumps(bsonScripts)
        return jsonScripts

    def addTrainedChatModel(self, trainedChatModel):
        chatModelCollection = self.db[self.trainedChatCollection]
        chatModelCollection.insert_one(trainedChatModel)


    def getTrainedChatModelById(self, id):
        chatModelCollection = self.db[self.trainedChatCollection]
        bsonChatModel = chatModelCollection.find_one({"_id": id})
        jsonChatModel = dumps(bsonChatModel)
        return jsonChatModel

    def getNextTrainedModelId(self):
        chatModelCollection = self.db[self.trainedChatCollection]
        bsonChatId = chatModelCollection.find({}, {"_id": 1}).sort("_id").limit(1)
        jsonChatId = dumps(bsonChatId[0])
        idDIct = json.loads(jsonChatId)
        return idDIct["_id"]

