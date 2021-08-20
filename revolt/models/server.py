


class Server :
    """ represents the server object"""

    def __init__(self , event):
        self.id = event["id"]
        self.nonce = event.get("nonce" , None)
        self.owner = event["owner"]
        self.name = event["name"] 
        self.description = event.get("description" , None)
        self.channel_ids = event["channels"]
        categories = event.get("categories" , [])
        self.categories = []
        for category in categories :
            self.categories.append(Category(category))

        #TODO complete this stuff 


            
       






class Category :
    """represents the server category object"""
    def __init__(self,category_dict):
        self.id = category_dict["id"]
        self.title = category_dict["title"]
        self.channels = category_dict["channels"]

