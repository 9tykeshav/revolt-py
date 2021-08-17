from revolt.bot import Bot
import json
import asyncio
from dotenv import load_dotenv 
import os 


load_dotenv()
TOKEN = os.getenv("TOKEN")

client = Bot()


   #res = await a.http.send_message("01FD5A94JN4YQZ5BR722Q606YX" , "amongus" )
   #print(res)

@client.event
async def authenticate (ctx) : 
    print("we have been successfully authencated to thewebsocket")
    print(ctx)


@client.event
async def ready(ctx) : 
    print(ctx)

client.run(TOKEN)
