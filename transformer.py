import pandas as pd
import numpy as np

class Transformer:

    seperator = " ++++ "
    headers = ['individual', 'content']

    def transformChatMatrixByMessageAsDF(self, text):

        allMessages = []
        for message in text.messagelog:
            messageContent = ' '.join(message.content)
            fullMessage = [message.sender, messageContent]
            allMessages.append(fullMessage)

        df = pd.DataFrame.from_records(allMessages, columns=self.headers)
        df.set_index(self.headers[0], inplace=True)

        return df

    def transformChatMatrixBySenderAsDF(self, text):
        allParticipants = {}
        for message in text.messagelog:
            messageContent = ' '.join(message.content)
            if(message.sender in allParticipants):
                currentWords = allParticipants[message.sender]
                currentWords = currentWords + ' ' + messageContent
                allParticipants[message.sender] = currentWords
            else:
                allParticipants[message.sender] = messageContent

        df = pd.DataFrame.from_dict(allParticipants, orient='index', columns=[self.headers[1]])
        df.index.name = self.headers[0]
        return df


    def transformMovieMatrixAsDF(self, movie):
        allMovieChars = []
        for character in movie.characters:
           charPlaceholder = character.name + self.seperator + movie.name + self.seperator + str(movie.id)
           allMovieChars.append((charPlaceholder, self.__combineWordLists(character.lines)))

        df = pd.DataFrame.from_records(allMovieChars, columns=self.headers)
        df.set_index(self.headers[0], inplace=True)

        return df

    def transformMoviesMatrixAsDF(self, movies):
        alldf = []
        for i in range(0, len(movies)):
            df = self.transformMovieMatrixAsDF(movies[i])
            alldf.append(df)

        return pd.concat(alldf)

    def __combineWordLists(self, wordLists):
        allWords = []
        for wordList in wordLists:
            for word in wordList:
                allWords.append(word)
        return  ' '.join(allWords)

