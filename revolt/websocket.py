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
        auth_dict = {'type': 'Authenticate',
    'token': self.client.token
    }
        authentication = json.dumps(auth_dict)
        print("sending authenticate :" , authentication)
        await self.connection.send_str(authentication)

    async def start(self) :
        await self.authenticate()
        while True :
            event = await self.connection.receive()
            print(event) 


