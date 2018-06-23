from domain import Chat, Message

class ChatFactory:

    def createChat(self, chat):
        id = chat["_id"]
        name = chat["name"]
        messages = self.__createMessages(chat["messagelog"])

        return Chat(id, name, messages)

    def __createMessages(self, messageLog):
        messages = []
        for message in messageLog:
            sender = message["sender"]
            sendtime = message["sendtime"]["$date"]
            content = message["content"]
            messages.append(Message(sender, sendtime, content))

        return messages
