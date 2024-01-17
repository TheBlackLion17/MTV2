import asyncio
from pyrogram import Client, filters
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6663025289:AAEA_-gCBnIdV3TPGZ3CTnI78lvZqkWfep8")

API_ID = int(os.environ.get("API_ID", "20919286"))

API_HASH = os.environ.get("API_HASH", "57b85f72104db3f08f9795b0410eb556")

STRING = os.environ.get("STRING", "BQE_M_YAov_-48Y3a1LuI0Xe7do2XCh7lu1dodZoO1cTtR7xNKXcpguSuFDYxqvflFm4nPEeaC1a6gNNxtAj_-i3NuLIMv6MF-bpu71royeKlp7yUeG0Pe55kghXTLkp6ETpzeu27jsEiJCrJUbZ20ax9OrV9Mx4-urvf3yqLEXafVL6h6hV883q8pPVhYHxXX_Tm-LFuFWsCehZLVTlgNPyHnXXOEq_3aCp6sPybR265zLt0t9kVAnSd1JkUvNpp5d5Guu1XQ-K3LKePo3V9vqW__ohTC3xXJVVWoqi7CqzGfkTxxIt1McosfiQDDy5FnL2toBO1GQuXfhT5sRjU-2I1UdR0gAAAAGfW0-BAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
