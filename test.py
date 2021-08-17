from revolt.bot import Bot
import json
import asyncio
from dotenv import load_dotenv 
import os 
from collections import namedtuple

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
    print(dir(ctx)) 
    client.users = ctx.load_users()
    print(dir(client.users))
    print(client.users[0].username)
    await client.http.send_message("01FD5A94JN4YQZ5BR722Q606YX" , str(len(client.users)) )
    

client.run(TOKEN)
