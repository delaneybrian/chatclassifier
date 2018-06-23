from domain import MovieCharacter, Movie

class MovieFactory:

    def createMovie(self, movie):
        characters = self.__createMovieCharacters(movie)
        return Movie(movie["_id"], movie["name"], characters)


    def __createMovieCharacters(self, movie):
        characters = []
        script = movie["script"]
        for character in script["characters"]:
            newCharacter = MovieCharacter(character["name"], character["lines"])
            characters.append(newCharacter)

        return characters
