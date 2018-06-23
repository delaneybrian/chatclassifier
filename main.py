from repository import Repository
from cleaner import Cleaner
from chatFactory import ChatFactory
from movieFactory import MovieFactory
from transformer import Transformer
from textProcessor import TextProcessor

def main():

    cleaner = Cleaner()
    repository = Repository()
    movieFactory = MovieFactory()
    chatFactory = ChatFactory()
    transformer = Transformer()
    textProcessor = TextProcessor()

    rawChat = repository.getChatById(1)
    rawMovie = repository.getMovieById(1)

    chat = chatFactory.createChat(rawChat)
    movie = movieFactory.createMovie(rawMovie)

    cleanedChat = cleaner.cleanChat(chat)
    cleanedMovie = cleaner.cleanMovie(movie)

    chatMatrix1 = transformer.transformChatMatrixByMessage(cleanedChat)
    chatMatrix2 = transformer.transformChatMatrixBySender(cleanedChat)
    movieMatrix = transformer.transformMovieMatrix(cleanedMovie)


    chat1 = textProcessor.createTFIDFMatrix(chatMatrix2)


    print("Finished")

if __name__ == "__main__":
    main()