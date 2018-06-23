from domain import Chat, Message, MovieCharacter, Movie

class Transformer:

    def transformChat(self, chat):
        id = chat["_id"]
        name = chat["name"]
        messageLog = self.__transformMessageLog(chat["messagelog"])

        return Chat(id, name, messageLog)

    def __transformMessageLog(self, messageLog):
        messages = []
        for message in messageLog:
            sender = message["sender"]
            sendtime = message["sendtime"]["$date"]
            content = message["content"]
            messages.append(Message(sender, sendtime, content))

        return messages

    def transformMovie(self, movie):
        characters = self.__transformMovieScript(movie)
        return Movie(movie["_id"], movie["name"], characters)


    def __transformMovieScript(self, movie):
        characters = []
        script = movie["script"]
        for character in script["characters"]:
            newCharacter = MovieCharacter(character["name"], character["lines"])
            characters.append(newCharacter)

        return characters
