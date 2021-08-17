from revolt.bot import Bot
import json
import asyncio
from dotenv import load_dotenv 
import os 


load_dotenv()
TOKEN = os.getenv("TOKEN")

a = Bot(TOKEN)

async def main () :
   res = await a.http.send_message("01FD5A94JN4YQZ5BR722Q606YX" , "amongus" )
   print(res)

asyncio.run(main())
