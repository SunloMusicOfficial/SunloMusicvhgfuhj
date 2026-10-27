import asyncio
import logging
from pyrogram import Client
from pytgcalls import PyTgCalls
from config import config
from database import db
from helpers.decorators import load_commands

# Logging Setup (Premium JSON-like format)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S"
)

# 1. Main Bot (Jo commands sunega)
app = Client(
    "SunloMusicBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# 2. Assistant Userbot (Jo Voice Chat join karega aur gaana bajayega)
userbot = Client(
    "SunloMusicAssistant",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    session_string=config.SESSION_STRING
)

# 3. PyTgCalls Engine (Streaming)
call = PyTgCalls(userbot)

# Ek dusre se connect karna
app.call = call
app.userbot = userbot
app.db = db

async def start_bot():
    logging.info("⏳ Starting SunloMusic...")
    
    # Database connect karo
    await db.connect()
    
    # Assistant aur Call engine start karo
    await userbot.start()
    await call.start()
    
    # Main Bot start karo
    await app.start()
    
    # Saare commands auto-load karo
    load_commands()
    
    logging.info(f"🎵 {config.BOT_NAME} is LIVE and Ready!")
    
    # Bot ko chalta hua rakho
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        app.loop.run_until_complete(start_bot())
    except KeyboardInterrupt:
        logging.info("🛑 Bot Stopped manually.")
    except Exception as e:
        logging.error(f"❌ Fatal Error: {e}")
