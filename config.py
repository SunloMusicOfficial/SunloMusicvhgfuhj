import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    SESSION_STRING = os.getenv("SESSION_STRING", "")
    
    MONGO_URL = os.getenv("MONGO_URL", "")
    REDIS_URL = os.getenv("REDIS_URL", "")
    
    OWNER_ID = int(os.getenv("OWNER_ID", "0"))
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "0"))
    
    # Branding
    BOT_NAME = "SunloMusic"
    BOT_USERNAME = "@SunloMusicBot"
    SUPPORT_CHAT = "https://t.me/Vip_Sakil_Bio"
    DEVELOPER = "@YO_UR_OFFICIAL_CRUSH"

config = Config()
