import aiohttp
import json




class Ws :
    """websocket handler"""

    def __init__(self , client) : 
        self.client = client 
        self.session = aiohttp.ClientSession()
        
        

    async def connect(self) :

        self.connection = await self.session.ws_connect("wss://ws.revolt.chat")

    async def authenticate(self):
        authentication = f"""{
    "type": "Authenticate",
    "token": f"self.client.token"
}"""
        self.connection.send_str(authentication)

    async def start(self) :
        self.authenticate()
        while True :
            event = await self.connection.recieve()
            print(event) 
            


