import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from domain import MovieCharacter, Movie, Chat, Message

class Cleaner:

    maxTokenLen = 20
    minTokenLen = 3
    maxNonEngChars = 5
    englishLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

    def cleanMovie(self, movie):
        cleanedCharacters = []
        for character in movie.characters:
            cleanedLines = []
            for line in character.lines:
                cleanedLine = self.__cleanMessage(line)
                if(len(cleanedLine) > 0):
                    cleanedLines.append(self.__cleanMessage(line))
            cleanedCharacters.append(MovieCharacter(character.name, cleanedLines))

        return Movie(movie.id, movie.name, cleanedCharacters)

    def cleanChat(self, chat):
        cleanedMessageLog = []
        for message in chat.messagelog:
            cleanedContent = self.__cleanMessage(message.content)
            if(len(cleanedContent) > 0):
                cleanedMessageLog.append(Message(message.sender, message.sendtime, cleanedContent))

        return Chat(chat.id, chat.name, cleanedMessageLog)




    def __cleanMessage(self, rawtext):
        tokens = self.__tokenise(rawtext)
        tokens = self.__normalise(tokens)
        tokens = self.__removeSpecialCharacters(tokens)
        tokens = self.__removeStopWords(tokens)
        tokens = self.__stem(tokens)
        tokens = self.__removeSingles(tokens)
        tokens = self.__removeLongWords(tokens)
        tokens = self.__removeShortWords(tokens)
        tokens = self.__removeNonEnglishWords(tokens)
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

    def __removeLongWords(self, tokens):
        noLongWords = []
        [noLongWords.append(token) for token in tokens if len(token) < self.maxTokenLen]
        return noLongWords

    def __removeShortWords(self, tokens):
        noShortWords = []
        [noShortWords.append(token) for token in tokens if len(token) > self.minTokenLen]
        return noShortWords

    def __removeNonEnglishWords(self, tokens):
        noNonEnglish = []
        for token in tokens:
            numNonEng = 0
            chars = list(token)
            for char in chars:
                if char not in self.englishLetters:
                    numNonEng += 1
            if(numNonEng < self.maxNonEngChars):
                noNonEnglish.append(token)

        return noNonEnglish

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

