from repository import Repository
from cleaner import Cleaner
from chatFactory import ChatFactory
from movieFactory import MovieFactory
from transformer import Transformer
from textProcessor import TextProcessor
from model import Model

def main():

    cleaner = Cleaner()
    repository = Repository()
    movieFactory = MovieFactory()
    chatFactory = ChatFactory()
    transformer = Transformer()
    textProcessor = TextProcessor()
    model = Model()

    rawChat = repository.getChatById(2)
    rawMovie1 = repository.getMovieById(1)
    rawMovie2 = repository.getMovieById(6)

    chat = chatFactory.createChat(rawChat)
    movie1 = movieFactory.createMovie(rawMovie1)
    movie2 = movieFactory.createMovie(rawMovie2)

    cleanedChat = cleaner.cleanChat(chat)
    cleanedMovie1 = cleaner.cleanMovie(movie1)
    cleanedMovie2 = cleaner.cleanMovie(movie2)

    chatMatrix1 = transformer.transformChatMatrixByMessageAsDF(cleanedChat)
    chatMatrix = transformer.transformChatMatrixBySenderAsDF(cleanedChat)

    #moviedf = transformer.transformMoviesMatrixAsDF([cleanedMovie1, cleanedMovie2])
    textProcessor.create_tfidf_from_dataframe(chatMatrix1)

    #chat1 = textProcessor.createTFIDFMatrix(chatMatrix2)

    #model.trainChatClassifier(chat1)


    print("Finished")

if __name__ == "__main__":
    main()