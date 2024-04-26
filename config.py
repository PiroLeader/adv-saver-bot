from os import environ 

class Config:
    API_ID = environ.get("API_ID", "18429621")
    API_HASH = environ.get("API_HASH", "2034b81303744d1dd2c7ffc02e21cfe2")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6919931089:AAEf3J_XJqVq019hzlxd6eCwHvzpOdrnjXA") 
    BOT_SESSION = environ.get("BOT_SESSION", "AQEZNrUAgwzGUEXbTerKwYugN_pG1InjQWyiEULb5z7XHdOfb5CtWAr3QyIsuG9Ma9IazV7K3I5NJRdybdgDhTscd3qxcxQZKhZ17v31ksOiOEh4YSUovFnw8-uv_dbzkwimLEk2QYwL3ZP6hrZoy_BC4xkuvuxfltuz14CRyJf15Ob8QBsshh1QFRZzjJMPKsO6jW67IpKriiL0mRIxk7bjkAq6OTp2Yah_yPOJYBt2ST5jq3868gitzr7MEV7vkhz4L9x496dvgCN0cD3PM9HA2veaZXxJoKKwdAq_N25c1QGTNfoQo5VfeCTvXMwCZZXqGhWL5xOLUf6ESAMRk9HL5qSS7AAAAAFHC6iRAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://NoMoreLeader:leadernomore@trialfilterdb.c46bglu.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5486913681').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
