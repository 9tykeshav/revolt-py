import aiohttp
import json




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

    async def start(self) :
        """starts a loop and listens to the events"""


        await self.authenticate()
        while True :
            event = await self.connection.receive()
            if event.type ==  aiohttp.WSMsgType.TEXT :
                event_json = json.loads(event.data)
                if event_json["type"] == "Authenticated":
                    await self.client.call_event("authenticate" , None)
                elif event_json["type"] == "Ready" :
                    await self.client.call_event("ready" , event_json)
                else :
                    print(event)
            else :
                print("we got something we dont know")

            #TODO HANDLE THE STUFF HERE


