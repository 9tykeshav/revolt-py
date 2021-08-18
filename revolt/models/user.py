import json
import aiohttp



class User:

    """represents a user"""

    def __init__(self , user_dict) :
        self.id = user_dict.get("_id" , None)
        self.username = user_dict.get("username" ,None)
        #TODO fix this mess 
        if user_dict.get("avatar" , None) :

            self.avatar_id = user_dict["avatar"]["_id"]
            self.avatar_size = user_dict["avatar"]["size"]

            self.avatar_tag = user_dict["avatar"]["tag"]

        else :
            self.avatar_id = None
            self.avatar_size = None
            self.avatar_tag = None
            self.relationship = user_dict.get("relatioship" ,None)
        self.badges = user_dict.get("badges" , None)
        self.flags = user_dict.get("flags" , None)
        self.online = user_dict.get("online" , None)
