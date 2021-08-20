import json


class Message :
    """represents the message object"""

    def __init__(self ,event):
        self.event = event
        self.id = event["_id"]
        self.content = event.get("content" , None)
        self.nonce = event.get("nonce" , None)
        self.channel = event.get("channel" , None)
        self.author_id = event["author"]
        #TODO complete 

