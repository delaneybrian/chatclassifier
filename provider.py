from cleaner import Cleaner
from chatFactory import ChatFactory
from movieFactory import MovieFactory
from model import Model
from repository import Repository
from transformer import Transformer
from comparer import Comparer

class Provider:

    cleaner = Cleaner()
    repository = Repository()
    movieFactory = MovieFactory()
    chatFactory = ChatFactory()
    transformer = Transformer()
    model = Model()
    comparer = Comparer()

    def train_chat_model(self, chatId):
        rawChat = self.repository.getChatById(chatId)
        chat = self.chatFactory.createChat(rawChat)
        cleanedChat = self.cleaner.cleanChat(chat)
        chatMatrix1 = self.transformer.transformChatMatrixByMessageAsDF(cleanedChat)
        self.model.create_chat_model_from_dataframe(chatMatrix1, chatId)

    def make_prediction_from_chat_model(self, chatId, message):
        return self.model.make_prediction_from_model(chatId, message)

    def add_new_movies_df(self):
        self.comparer.create_all_movies_df()

    def find_movie_comparisons_from_chat(self, chatId):
        rawChat = self.repository.getChatById(chatId)
        chat = self.chatFactory.createChat(rawChat)
        cleanedChat = self.cleaner.cleanChat(chat)
        chatMatrix = self.transformer.transformChatMatrixBySenderAsDF(cleanedChat)
        chatMovieDf = self.comparer.create_chat_movie_df(chatMatrix)

        comparison = self.comparer.generate_comparison(chatMovieDf, chatMatrix)
        return comparison