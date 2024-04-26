from os import environ 

class Config:
    API_ID = environ.get("API_ID", "18429621")
    API_HASH = environ.get("API_HASH", "2034b81303744d1dd2c7ffc02e21cfe2")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6919931089:AAEf3J_XJqVq019hzlxd6eCwHvzpOdrnjXA") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://NoMoreLeader:leadernomore@trialfilterdb.c46bglu.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5486913681').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
