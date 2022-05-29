from os import environ
from pyrogram import Client, filters
from pyrogram.types import *

pr0fess0r_99 = Client("ShareText-Bot",
    api_id=environ["API_ID"], api_hash=int(environ["API_HASH"]), bot_token=environ["BOT_TOKEN"])

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    pr0fess0r99 = InlineKeyboardMarkup( [[ InlineKeyboardButton("📦 Source Code 📦", url="https://github.com/PR0FESS0R-99/ShareText-Bot") ]] )
    await bot.send_message(chat_id="me",
        text=f"Hey {update.from_user.mention}\n" + "Iam A Telegram Text Message Sharing Link Creating Bot" + "\n" + "Maintained By [MoTech](t.me/mo_Tech_Group)",
        reply_markup=pr0fess0r99, disable_web_page_preview=True, reply_to_message_id=update.id
    )
