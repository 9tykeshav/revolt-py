import aiohttp
import json
import asyncio
from .models.ready import Ready
class Ws :
    """websocket handler"""

    def __init__(self , client) : 
        self.client = client 
        self.session = aiohttp.ClientSession()
        
        

    async def connect(self) :
        """connects the bot to the websocket"""

        self.connection = await self.session.ws_connect("wss://ws.revolt.chat")

    async def authenticate(self):
        """constructs and sends the authenticate event"""
        auth_dict = {'type': 'Authenticate',
    'token': self.client.token
    }
        self.authentication = json.dumps(auth_dict)
        #TODO setup logger for below statement 
        print("sending authenticate :" , self.authentication)
        await self.connection.send_str(self.authentication)

    async def heartbeat(self) :
        while True :
            await asyncio.sleep(13) 
            await self.connection.ping(b'amogus')

    async def start(self) :
        """starts a loop and listens to the events"""

        #TODO manage stuff so that hearbeat is only called on successfull authentication 

        await self.authenticate()
        asyncio.create_task(self.heartbeat())

        while True :
            
            event = await self.connection.receive()
            if event.type ==  aiohttp.WSMsgType.TEXT :
                event_dict = json.loads(event.data)
                if event_dict["type"] == "Authenticated":
                    await self.client.call_event("authenticate" , None)
                elif event_dict["type"] == "Ready" :
                    await self.client.call_event("ready" , Ready(event_dict))
                else :
                    print(event)
            else :
                print(event)
                

            #TODO HANDLE THE STUFF HERE


