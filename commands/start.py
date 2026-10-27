from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import config

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client: Client, message: Message):
    # Premium Welcome Text
    text = f"""
✨ **Welcome to {config.BOT_NAME}** ✨
━━━━━━━━━━━━━━━━━━━━━━
Hey {message.from_user.mention}! 
Main ek advanced, ultra-fast music bot hoon. Mujhe apne group mein add karo aur high-quality music ka maza lo. 🎧

🎛 **Features:**
• Lossless Audio & Fast Streaming
• 24/7 Voice Chat Support
• Premium UI & Controls
• No Lag, No Ads!

💡 **Kaise use karein?**
Mujhe group mein add karo, admin banao, aur `/play song_name` bhejo.
"""
    
    # Attractive Buttons
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("➕ Add me to Group", url=f"https://t.me/{config.BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("📢 Channel", url=config.SUPPORT_CHAT),
            InlineKeyboardButton("👨‍💻 Developer", url=f"https://t.me/{config.DEVELOPER.replace('@', '')}")
        ],
        [
            InlineKeyboardButton("🛠 Help & Commands", callback_data="help_menu")
        ]
    ])
    
    # Ek dummy image URL (baad mein custom image laga sakte hain)
    await message.reply_photo(
        photo="https://graph.org/file/ea2c902d6d3bc3d4e23b5.jpg", 
        caption=text,
        reply_markup=buttons
    )

@Client.on_message(filters.command("start") & filters.group)
async def start_group(client: Client, message: Message):
    text = f"👋 Hello {message.from_user.mention}!\nMain **{config.BOT_NAME}** hoon. Gaana bajane ke liye `/play` use karo.\n\nKoi dikkat ho toh admin se poocho ya /help bhejo."
    await message.reply_text(text)
