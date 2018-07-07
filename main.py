
def main():

    cleaner = Cleaner()
    repository = Repository()
    movieFactory = MovieFactory()
    chatFactory = ChatFactory()
    transformer = Transformer()
    model = Model()

    comparer = Comparer()

    rawChat = repository.getChatById(2)
    chat = chatFactory.createChat(rawChat)
    cleanedChat = cleaner.cleanChat(chat)
    chatMatrix1 = transformer.transformChatMatrixBySenderAsDF(cleanedChat)
    chatMovieDf = comparer.create_chat_movie_df(chatMatrix1)

    print(chatMovieDf.head(100))

    #comparer.create_all_movies_df()

    """
    #Chat Stuff
    rawChat = repository.getChatById(2)
    chat = chatFactory.createChat(rawChat)
    cleanedChat = cleaner.cleanChat(chat)
    chatMatrix1 = transformer.transformChatMatrixByMessageAsDF(cleanedChat)
    model.create_chat_model_from_dataframe(chatMatrix1, 1)
    #print(model.make_prediction_from_model("why does it always rain on poor old dan smyth who knows its cause it the slick bugger", 1))
    """

    print("Finished")

if __name__ == "__main__":
    main()