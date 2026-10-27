import importlib, pkgutil, logging
from functools import wraps
from pyrogram import enums
from pyrogram.types import Message

def load_commands():
    """Commands folder ko automatically load karega"""
    for _, module_name, _ in pkgutil.iter_modules(["commands"]):
        try:
            importlib.import_module(f"commands.{module_name}")
            logging.info(f"⚡ Loaded: {module_name}")
        except Exception as e:
            logging.error(f"❌ Failed to load {module_name}: {e}")

def admin_only(func):
    """Check karega ki user admin hai ya nahi"""
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            try:
                member = await client.get_chat_member(message.chat.id, message.from_user.id)
                if member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
                    return await message.reply("🚫 **Sirf Admins** ye command use kar sakte hain!")
            except Exception as e:
                pass 
        return await func(client, message, *args, **kwargs)
    return wrapper

def premium_only(func):
    """Future me Premium users check karne ke liye placeholder"""
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        # Abhi ke liye sabko allow kar rahe hain, baad me DB check lagega
        return await func(client, message, *args, **kwargs)
    return wrapper
