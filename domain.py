
class Chat:

    id = None
    name = None
    messagelog = None

    def __init__(self, id, name, messagelog):
        self.id = id
        self.name = name
        self.messagelog = messagelog

    def __str__(self):
        return "%s - %s" % (self.id, self.name)



class Message:

    sender = None
    sendtime = None
    content = None

    def __init__(self, sender, sendtime, content):
        self.sender = sender
        self.sendtime = sendtime
        self.content = content

    def __str__(self):
        return "%s - %s : %s" % (self.sender, self.sendtime, self.content)

class Script:

    def __init__(self):
        pass
