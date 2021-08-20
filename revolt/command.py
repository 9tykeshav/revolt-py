



class Command:
    """command object"""

    def __init__(self, **kwargs ):
        self.name = kwargs.pop("name")
        self.func = kwargs.pop("func") 
        self.aliases = kwargs.pop("alias" , [])


    def call(self):
        return self.func

    def aliases(self):
        return aliases 
        

    
