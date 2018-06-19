from repository import Repository
from cleaner import Cleaner
from transformer import Transformer
from textProcessor import TextProcessor
import json

def main():

    cleaner = Cleaner()
    repository = Repository()
    transformer = Transformer()


    chat = repository.getChatById(1)
    chatdata = json.loads(chat)

    transformedChat = transformer.transformChat(chatdata)

    print(transformedChat)
    for message in transformedChat.messagelog:
        print(message)

"""
    dict = {}
    dict["_id"] = 4
    dict["4"] = "james"
    dict["3"] = "carl"
    dict["2"] = "brian"
    dict["1"] = "tony"

    print(repository.getNextTrainedModelId())
"""

"""
    cleaner = Cleaner()

    message2 = "I went to Japan When I was young"
    message3 = "We travel alot when we are young"
    message4 = "It was a good place to travel to"
    message5 = "too many cooks spoil the broth"

    messages = []
    messages.append(cleaner.cleanMessage(message2))
    messages.append(cleaner.cleanMessage(message3))
    messages.append(cleaner.cleanMessage(message4))
    messages.append(cleaner.cleanMessage(message5))

    processor = TextProcessor()
    setDict = processor.calculateTFIDF(messages)
    print(setDict)
"""


if __name__ == "__main__":
    main()