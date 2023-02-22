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


MY_PASS = os.environ.get("MY_PASS", None)
pass_dict = {}
pass_db = Database(Var.DATABASE_URL, "ag_passwords")


@StreamBot.on_message(filters.command("stream") & filters.private)
async def media_receive_handler(_, m: Message):
    
    log_msg = await m.reply_to_message.forward(chat_id=Var.BIN_CHANNEL)
    stream_link = f"{Var.URL}{log_msg.id}/watch/{quote_plus(get_name(m.reply_to_message))}?hash={file_hash}"
    logger.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    await m.reply_text(
        text=f"Short Link : {short_link}",
        quote=True,
        parse_mode=ParseMode.HTML,
        reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Stream", url = stream_link)
      ]]
  )
    )

