import json
import aiohttp



class Ready:
    """Represents the data returned by ready event"""

    def __init__(self , event):
        self.event = event

    def load_users(self) :
        users = []

        for user in self.event["users"] :
            users.append(User(user))
        return users





class User:
    """represents a user"""

    def __init__(self , user_dict) :
        self.id = user_dict.get("_id" , None)
        self.username = user_dict.get("username" ,None)
        if user_dict.get("avatar" , None) :
            #TODO THIS IS A MESS FIX IT 

            self.avatar_id = user_dict["avatar"]["_id"] 
            self.avatar_size = user_dict["avatar"]["size"]
            self.avatar_tag = user_dict["avatar"]["tag"]
        else :
            self.avatar_id = None 
            self.avatar_size = None                  
            self.avatar_tag = None

        self.relationship = user_dict.get("relationship" ,None)
        self.badges = user_dict.get("badges" , None)
        self.flags = user_dict.get("flags" , None)
        self.online = user_dict.get("online" , None)





