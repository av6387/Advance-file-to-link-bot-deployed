#(c) Adarsh-Goel
import os
import asyncio
from asyncio import TimeoutError
from Adarsh.bot import StreamBot
from Adarsh.utils.database import Database
from Adarsh.utils.human_readable import humanbytes
from Adarsh.vars import Var
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)



@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def start(c: Client, m: Message):

        log_msg = await m.copy(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"

        msg_text ="""<b>✨✨ </b> <code>{}</code>\nℂ𝕙𝕒𝕟𝕟𝕖𝕝 -» @Classroom_lecturesS\n#Amit"""

        await log_msg.reply_text(text=f"**RᴇQᴜᴇꜱᴛᴇᴅ ʙʏ :** [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n**Uꜱᴇʀ ɪᴅ :** `{m.from_user.id}`\n**Stream ʟɪɴᴋ :** {stream_link}", disable_web_page_preview=True,  quote=True)
        await m.edit_text(
            text=msg_text.format((log_msg.caption and log_msg.caption.html), humanbytes(get_media_file_size(m)), online_link, stream_link),
       #     quote=True,
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
               [[
                        InlineKeyboardButton('DOWNLOAD 📥', url=online_link), #Download Link
                        InlineKeyboardButton("STREAM 🖥", url=stream_link) #Stream Link
               ]]
            )
        )
