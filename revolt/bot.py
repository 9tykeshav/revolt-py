import asyncio
import aiohttp
from .https import Http 



class Bot:
    """represents the basic bot class"""

    def __init__(self , token):
        self.token = token
        self.http = Http(self.token) 

        
