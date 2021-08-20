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
    print("we have been successfully auth-ed to thewebsocket")
    print(ctx)


@client.event
async def ready(ctx) :
    await asyncio.sleep(5) 
    print(json.dumps(ctx.event , indent = 2)) 
    client.users = ctx.load_users()
    print(dir(client.users))
    print(client.users[0].username)
    await client.http.send_message("01FD5A94JN4YQZ5BR722Q606YX" , str(len(client.users)) )


@client.command(name="owl" , alias=["test" , "nu"])
async def amogus(msg):
    await client.http.send_message(msg.channel ,"sus")

@client.command(name="sleep" , alias=["night", "gn"])
async def sleeper(msg):
    await client.http.send_message(msg.channel, "i am ssleeping")
    await asyncio.sleep(4)
    await client.http.send_message(msg.channel, "i wok up!!!!")

@client.event
async def message(msg):
    pass 




client.run(TOKEN)
