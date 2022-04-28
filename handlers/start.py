import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━
 ʜᴇYa  {message.from_user.mention()} !

   I Am Akira Music Player, a Powerful and fully lag free music player for Telegram groups...
Inspired by many open source projects...I provide the quality music playing solutions
to Telegram users.

*Note*- Add me to your group and make me admin to work me properly.


━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ADD AKIRA TO YOUR GROUP", url=f"https://t.me/Akira_MusicBot?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "⚡ Akira Official ⚡", url=f"https://t.me/Akira_Updates"
                    ),
                    InlineKeyboardButton(
                        "🔥 Creator 🔥", url=f"https://t.me/AkHiL_SI"
                    )
                    )]
            ]
       ),
    )

