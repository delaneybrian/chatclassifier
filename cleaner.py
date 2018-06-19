import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

class Cleaner:

    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def cleanMessage(self, rawtext):
        tokens = self.__tokenise(rawtext)
        tokens = self.__normalise(tokens)
        tokens = self.__removeSpecialCharacters(tokens)
        tokens = self.__removeStopWords(tokens)
        tokens = self.__stem(tokens)
        tokens = self.__removeSingles(tokens)
        return tokens

    def __tokenise(self, rawtext):
        return nltk.word_tokenize(rawtext)

    def __normalise(self, tokens):
        normalised = []
        for token in tokens:
            normalised.append(token.lower())
        return normalised

    def __removeSingles(self, tokens):
        noSingles = []
        for token in tokens:
            if len(token) > 1:
                noSingles.append(token)
        return noSingles

    def __removeStopWords(self, tokens):
        stopwds = stopwords.words('english')
        removed = []
        [removed.append(token) for token in tokens if token not in stopwds]
        return removed

    def __removeSpecialCharacters(self, tokens):
        specialchars = ['.', '!', '?', ',', "'"]
        for specialchar in specialchars:
            while specialchar in tokens: tokens.remove(specialchar)
        return tokens

    def __stem(self, tokens):
        stemmed = []
        stemmer = PorterStemmer()
        [stemmed.append(stemmer.stem(word)) for word in tokens]
        return stemmed

