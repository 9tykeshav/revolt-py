import aiohttp
import os 
import json 

class Http:
    """represents the http client"""

    def __init__(self , token , session = None):
        self.token = token
        #self.session = session if session else aiohttp.ClientSession()
        self.base_url = "https://api.revolt.chat/" 
        self.headers = { "x-bot-token" : self.token ,"content-Type" : "application/json" }


    async def request(self , payload , route , method):
        """ contructs the request and executes it"""

        async with aiohttp.ClientSession() as session:
            res = await session.request(method , self.base_url + route , json=payload, headers=self.headers) 
            return await res.json()
            await session.close()




    async def send_message(self,channel_id , content) :
        """send message functions / sends message to the channel id with content"""
        
        payload = {
            "content" : content , 
            "nonce" : str(os.urandom(8))
            }
        

        res = await self.request(payload=payload , route= f"channels/{channel_id}/messages" , method = "POST")
        return res  


            

