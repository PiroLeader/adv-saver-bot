#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "18429621" #config("API_ID", default=None, cast=int)
API_HASH = "2034b81303744d1dd2c7ffc02e21cfe2" #config("API_HASH", default=None)
BOT_TOKEN = "6919931089:AAEf3J_XJqVq019hzlxd6eCwHvzpOdrnjXA" #config("BOT_TOKEN", default=None)
SESSION = "AQEZNrUAgwzGUEXbTerKwYugN_pG1InjQWyiEULb5z7XHdOfb5CtWAr3QyIsuG9Ma9IazV7K3I5NJRdybdgDhTscd3qxcxQZKhZ17v31ksOiOEh4YSUovFnw8-uv_dbzkwimLEk2QYwL3ZP6hrZoy_BC4xkuvuxfltuz14CRyJf15Ob8QBsshh1QFRZzjJMPKsO6jW67IpKriiL0mRIxk7bjkAq6OTp2Yah_yPOJYBt2ST5jq3868gitzr7MEV7vkhz4L9x496dvgCN0cD3PM9HA2veaZXxJoKKwdAq_N25c1QGTNfoQo5VfeCTvXMwCZZXqGhWL5xOLUf6ESAMRk9HL5qSS7AAAAAFHC6iRAA" #config("SESSION", default=None)
FORCESUB = "TheNostalgiacBro" #config("FORCESUB", default=None)
AUTH = "5486913681" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
