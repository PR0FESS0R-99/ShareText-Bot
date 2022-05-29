from os import *
from urllib.parse import *
from pyrogram.types import *
from pyrogram import Client, filters

pr0fess0r_99 = Client("ShareText-Bot",
    api_id=int(environ["API_ID"]), api_hash=environ["API_HASH"], bot_token=environ["BOT_TOKEN"])

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    pr0fess0r99 = InlineKeyboardMarkup( [[ InlineKeyboardButton("📦 Source Code 📦", url="https://github.com/PR0FESS0R-99/ShareText-Bot") ]] )
    await bot.send_message(chat_id="me",
        text=f"Hey {update.from_user.mention}\n" + "Iam A Telegram Text Message Sharing Link Creating Bot" + "\n" + "Maintained By [MoTech](t.me/mo_Tech_Group)",
        reply_markup=pr0fess0r99, disable_web_page_preview=True, reply_to_message_id=update.id
    )

@pr0fess0r_99.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def sharelink(bot, update):
    await bot.send_message(chat_id="me",
        text=f"Message Sharing Link Is Ready :- https://t.me/share/url?url={quote(update.text)}",
        disable_web_page_preview=True, reply_to_message_id=update.id
    )

print("~~~~~~~~~~~")
print("Bot Started")
print("~~~~~~~~~~~")

pr0fess0r_99.run()
