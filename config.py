import os

class Config:
    API_ID = os.environ.get("API_ID", "22923037")
    API_HASH = os.environ.get("API_HASH", "dfb3666878b3851460a58461c5a50f5b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7704111228:AAH99yiMvuQ8tiy9l8eDw0-NXgOHzaTGkVc") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("6554343173", '').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    







    
    
    
    
    
    # Jishu Developer 
