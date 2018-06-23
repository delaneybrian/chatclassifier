class Transformer:

    seperator = " ++++ "

    def transformChatMatrixByMessage(self, text):
        allMessages = []
        for message in text.messagelog:
           allMessages.append((message.sender, message.content))

        return allMessages

    def transformChatMatrixBySender(self, text):
        allParticipants = {}
        for message in text.messagelog:
            if(message.sender in allParticipants):
                currentWords = allParticipants[message.sender]
                for word in message.content:
                    currentWords.append(word)
                allParticipants[message.sender] = currentWords
            else:
                allParticipants[message.sender] = message.content

        allParticipantsList = []
        for key in allParticipants.keys():
            allParticipantsList.append((key, allParticipants[key]))

        return allParticipantsList

    def transformMovieMatrix(self, movie):
        allMovieChars = []
        for character in movie.characters:
           charPlaceholder = character.name + self.seperator + movie.name + self.seperator + str(movie.id)
           allMovieChars.append((charPlaceholder, self.__combineWordLists(character.lines)))

        return allMovieChars

    def transformMoviesMatrix(self, movies):
        allMoviesChars = []
        for movie in movies:
            chars = self.createMovieMatrix(movie)
            for char in chars:
                allMoviesChars.append(char)

        return allMoviesChars

    def __combineWordLists(self, wordLists):
        allWords = []
        for wordList in wordLists:
            for word in wordList:
                allWords.append(word)
        return allWords

    def __combineOnParticipant(self):
        pass