import asyncio
import aiohttp
from .https import Http 
from .websocket import Ws 


class Bot:
    """represents the basic bot class"""

    def __init__(self):
        self.ws = Ws(self)
        self.events = {} # { func_name : func_object} 


    def event(self , func) :
        """decorator for events"""

        self.events[func.__name__] = func
        return func


    #TODO give good wording for the function
    async def _schedule_event(self ,event , ctx) :
        """constructs the event to be called for bot.call_event"""

        try :
            await event(ctx) 

        except Exception as e :
            print(str(e) + " at" , event)


    def call_event(self , event_name , ctx) :
        """calls the a event registered with @event"""

        event = self.events.get(event_name)
        if event :
            event_coro = self._schedule_event(event , ctx)
            asyncio.create_task(event_coro)

        else :
        #TODO have to return a error when events are called that  doesnt exits 
            #print("\n") 
           #print(self.events)
           pass 
        

    async def login(self) :
        """logs the bot In setups the http/websocket client"""

        self.http = Http(self.token)
        #TODO:REMOVE THE STUFF BELOW

        #await self.call_event("an_event" , "test ctx")


        ##REMOVE THE STUFF ABOVE
        await self.ws.connect()
        await self.ws.start()





    def run(self, token):
        """runs the bot"""

        self.token = token
        asyncio.get_event_loop().run_until_complete(self.login())
        


        
