from domain import Chat
from domain import Message

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
