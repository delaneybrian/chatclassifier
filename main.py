from repository import Repository
from cleaner import Cleaner
from textProcessor import TextProcessor
import json

def main():
    """
    repository = Repository()

    chat = repository.getChatById(1)
    chatdata = json.loads(chat)
    for message in chatdata["messagelog"]:
        print(cleaner.cleanMessage(message["content"]))
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



if __name__ == "__main__":
    main()