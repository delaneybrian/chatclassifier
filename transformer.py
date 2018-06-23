import pandas as pd
import math

class TextProcessor:

    seperator = " ++++ "

    def createChatMatrixByMessage(self, text):
        allMessages = []
        for message in text.messagelog:
           allMessages.append((message.sender, message.content))

        print(allMessages)

    def createChatMatrixBySender(self, text):
        allParticipants = {}
        for message in text.messagelog:
            if(message.sender in allParticipants):
                currentWords = allParticipants[message.sender]
                for word in message.content:
                    currentWords.append(word)
                allParticipants[message.sender] = currentWords
            else:
                allParticipants[message.sender] = message.content

        print(allParticipants)

    def createMovieMatrix(self, movie):
        allMovieChars = []
        for character in movie.characters:
           charPlaceholder = character.name + self.seperator + movie.name + self.seperator + movie.id
           allMovieChars.append((charPlaceholder, self.__combineWordLists(character.lines)))

        print(allMovieChars)

    def createMoviesMatrix(self, movies):
        allMoviesChars = []
        for movie in movies:
            chars = self.createMovieMatrix(movie)
            for char in chars:
                allMoviesChars.append(char)


    def __combineWordLists(self, wordLists):
        allWords = []
        for wordList in wordLists:
            for word in wordList:
                allWords.append(word)
        return allWords

    def __combineOnParticipant(self):
        pass