import pickle
from sklearn.naive_bayes import GaussianNB

class Model:

    def __init__(self):
        pass

    def trainMovieClassifier(self, movieMatrix):
        pass

    def trainChatClassifier(self, chatDataFrame):
        gnb = GaussianNB()

        print(chatDataFrame)

    def predictChat(self, modelId, data):
        pass

    def predictMovie(self, modelId, data):
        pass