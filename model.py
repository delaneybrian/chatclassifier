import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

class Model:

    def __init__(self):
        pass

    def trainMovieClassifier(self, movieMatrix):
        pass

    def trainChatClassifier(self, data, cats):
        knn = KNeighborsClassifier()
        knn.fit(data, cats)
        return knn

    def predictChat(self, modelId, data):
        pass

    def predictMovie(self, modelId, data):
        pass