from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime


START_TEXT = """ Your Telegram DC Is : `{}`  """


@StreamBot.on_message(filters.regex("Channels"))
async def maintainers(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="[Achiever Classroom Lectures](https://t.me/+Zi50V2vPxL8xNGJh)\n\n[Enthuse Classroom Lectures](https://t.me/+81ZPiZ8WRr83NDIx)\n\n[Nurture ClassroomLectures](https://t.me/+tDEZxSV4M8U1YjNh)",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Backup🔰", url=f"https://t.me/Classroom_lecturess")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
            
         
@StreamBot.on_message(filters.regex("Subscribe ❤️"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<B>HERE'S THE SUBSCRIBE LINK</B>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Subscribe ❤️", url=f"https://youtube.com/@AmitAD")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
        

@StreamBot.on_message(filters.regex("BOTS"))
async def start(bot, update):
    try:
   await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<B>HERE'S THE BOT LINK</B>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("BOT #1❤️", url=f"https://t.me/samit_07bot")
                                InlineKeyboardButton("BOT #2❤️", url=f"https://t.me/aaamit_02bot")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)

    
    
@StreamBot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = "Hi! {} Here is a list of all my commands \n \n 1 . `start⚡️` \n 2. `help📚` \n 3. `login🔑` \n 4.`Subscribe ❤️` \n 5. `ping📡` \n 6. `status📊` \n 7. `BOT` this tells your telegram dc \n 8. `Channel` "
    await l.send_message(chat_id = m.chat.id,
        text = LIST_MSG.format(m.from_user.mention(style="md"))
        
    )
    
    
@StreamBot.on_message(filters.regex("ping📡"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"Pong!\n{time_taken_s:.3f} ms")
    
    
    
    
@StreamBot.on_message(filters.private & filters.regex("status📊"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            f'<b>Total disk space:</b> {total}\n' \
            f'<b>Used:</b> {used}  ' \
            f'<b>Free:</b> {free}\n\n' \
            f'📊Data Usage📊\n<b>Upload:</b> {sent}\n' \
            f'<b>Down:</b> {recv}\n\n' \
            f'<b>CPU:</b> {cpuUsage}% ' \
            f'<b>RAM:</b> {memory}% ' \
            f'<b>Disk:</b> {disk}%'
  await update.reply_text(botstats)
