from pymongo import MongoClient
from bson.json_util import dumps
import json

class Repository:

    testCollection = "testcollection"
    movieCollection = "movietestcollection"
    trainedChatCollection = "testtrainedchatcollection"

    def __init__(self):
        self.client = MongoClient("mongodb://chatclassifieradmin:twilightstruggle1960@ds016128.mlab.com:16128/chatclassifier")
        self.db = self.client['chatclassifier']

    def getChatById(self, id):
        chatCollection = self.db[self.testCollection]
        bsonChat = chatCollection.find_one({"_id": id})
        jsonChat = dumps(bsonChat)
        pythonChat = json.loads(jsonChat)
        return pythonChat

    def getMovieById(self, id):
        movieCollection = self.db[self.movieCollection]
        bsonMovie = movieCollection.find_one({"_id": id})
        jsonMovie = dumps(bsonMovie)
        pythonMovie = json.loads(jsonMovie)
        return pythonMovie

    def getAllMovies(self):
        movieCollection = self.db[self.movieCollection]
        bsonMovies = movieCollection.find()
        jsonMovies = dumps(bsonMovies)
        return jsonMovies

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

