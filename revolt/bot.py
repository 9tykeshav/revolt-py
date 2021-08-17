import asyncio
import aiohttp
from .https import Http 
from .websocket import Ws 


class Bot:
    """represents the basic bot class"""

    def __init__(self):
        self.ws = Ws(self) 

    async def login(self) :
        
        self.http = Http(self.token)
        await self.ws.connect()
        await self.ws.start()

    def run(self, token):
        self.token = token

        asyncio.get_event_loop().run_until_complete(self.login())
        


        
