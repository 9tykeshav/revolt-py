import aiohttp
import json
import asyncio
from .models.ready import Ready
from .models.message import Message
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

    def _handle_commands(self , msg):
        """handles command"""

        if msg.content[0] == "!" :
            first_word = "".join(msg.content[1:].split(" "))
            for command in self.client.commands:
                for alias in command.aliases :
                    if first_word == alias:
                        asyncio.create_task(command.func(msg))
                        return 
                    
            asyncio.create_task(self.client.http.send_message(msg.channel , f"{first_word} : command not found"))



    async def heartbeat(self) :
        while True :
            await asyncio.sleep(13) 
            await self.connection.send_str('{"type" : "ping"}')


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
                    self.client.call_event("authenticate" , None)
                elif event_dict["type"] == "Ready" :
                    self.client.call_event("ready" , Ready(event_dict))
                elif event_dict["type"] == "Message" :
                    self.client.call_event("message" ,Message(event_dict))
                    self._handle_commands(Message(event_dict))



                else :
                    print(event)
            else :
                print(event)
                

            #TODO HANDLE THE STUFF HERE








