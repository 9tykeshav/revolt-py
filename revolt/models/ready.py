import json
import aiohttp
from .user import User



class Ready:
    """Represents the data returned by ready event"""

    def __init__(self , event):
        self.event = event

    def load_users(self) :
        users = []

        for user in self.event["users"] :
            users.append(User(user))
        return users







