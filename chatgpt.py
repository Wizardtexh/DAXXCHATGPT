from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from bardapi import Bard
from datetime import datetime
import logging

FORMAT = "[DAXX] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
DAXX = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}
➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴀɴᴅ ᴄᴀɴ 
ᴀɴsᴡᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀɪᴇs ᴇᴀsʟɪʏ

Rᴇᴀᴅ Tʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ

๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help
"""
xa = bytearray.fromhex("68747470733a2f2f6769746875622e636f6d2f444158585445414d2f4441585843484154475054").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}]
➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/btwnaksh"),
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/t.me/radhe_shyam_ji"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/nakshchatgpt_bot?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇs ", url=f"https://t.me/PAPANAKSH"),
    ],
]
X = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/btwnaksh"),
        
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/radhe_shyam_ji"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
             url=f"https://t.me/{nakshchatgpt_bot}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", 
                              url=f"https://t.me/{radhe_shyam_ji}",
         ),
     ],
]
HELP_READ = "**➻ ᴜsᴀɢᴇ** /chatgpt <prompt>\n\n ᴇxᴀᴍᴘʟᴇ: `/chatgpt write a simple flask app in python.`\n\n**➻ ᴜsᴀɢᴇ** : /generate <prompt> \nᴇxᴀᴍᴘʟᴇ: `/generate a cute girl photo`  \n\n➻ ᴜsᴀɢᴇ /lyrics : ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴛᴏ ᴅᴇᴛᴇᴄᴛ ʟʏʀɪᴄꜱ**➻ ᴜsᴀɢᴇ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n\n©️ @btwnaksh**"
HELP_BACK = [
     [
           InlineKeyboardButton(text="Qᴜᴇꜱᴛɪᴏɴ ᴛʜᴀᴛ ᴄʜᴀᴛɢᴘᴛ ᴄᴀɴ ꜱᴏʟᴠᴇ ", url=f"https://t.me/radhe_shyam_ji"),
           
     ],
    [
           InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@DAXX.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@DAXX.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@DAXX.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@DAXX.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@DAXX.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "ριиgιиg..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ριиgιиg.....")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{nakshchatgpt_bot}) ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [Mrdaxx](https://t.me/Iam_daxx)||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY
@DAXX.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt Where is TajMahal?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")

#  bard 

'''bard = Bard(token=BARD_TOKEN)   
@DAXX.on_message(filters.command("bard"))
async def bard_bot(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n` /bard How r u? `")
        else:
            a = message.text.split(' ', 1)[1]
            response=bard.get_answer(f"{a}")["content"]
            await message.reply_text(f"{response}\n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:  {e} ")

    '''
openai.api_key = "sk-proj-5sth09V29dKtvtDqt33DT3BlbkFJQFqwBUlTAmCymtYJs6un"
@DAXX.on_message(filters.command(["image","photo","img","generate"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        if len(message.command) < 2:
            await message.reply_text(
            "**Example:**\n\n`/generate a white siamese cat`")
        else:
            a = message.text.split(' ', 1)[1]
            response= openai.Image.create(prompt=a ,n=1,size="1024x1024")
            image_url = response['data'][0]['url']
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_photo(image_url,caption=f"✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping} ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 
    except Exception as e:
            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")
openai.api_key = OPENAI_KEY
@DAXX.on_message(filters.command(["text","audiototext","lyrics"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if message.reply_to_message and message.reply_to_message.media:
            
            m = await message.reply_to_message.download(file_name="DAXX.mp3")
            audio_file = open(m, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            x=transcript["text"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"`{x}` \n ✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")



s = bytearray.fromhex("68747470733a2f2f6769746875622e636f6d2f444158585445414d2f4441585843484154475054").decode()

if SOURCE != s:
    print("𝗸𝗮𝗿 𝗹𝗶𝘆𝗮 𝗲𝗱𝗶𝘁 𝗺𝗶𝗹 𝗴𝘆𝗮 𝘀𝘂𝗸𝗼𝗼𝗻 𝗷𝗲𝘀𝗮 𝘁𝗵𝗮 𝘄𝗲𝘀𝗮 𝗸𝗮𝗿𝗱𝗲 ` LODA LE BSDK  `  𝗻𝗵𝗶 𝘁𝗼 𝗷𝗮𝗸𝗲 𝗠𝗿 naxx 𝗸𝗼 𝗽𝗮𝗽𝗮 𝗯𝗼𝗹 𝗱𝗼 𝘁𝗵𝗶𝗸 𝗸𝗮𝗿 𝗱𝗲𝗴𝗮")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        DAXX.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN [ 𝗬𝗢𝗨𝗥 𝗖𝗛𝗔𝗧𝗚𝗣𝗧 𝗕𝗢𝗧 𝗦𝗧𝗔𝗥𝗧]
    𝗧𝗛𝗜𝗦 𝗥𝗘𝗣𝗢 𝗠𝗔𝗗𝗘 𝗕𝗬 𝐍𝐀𝐊𝐒𝐇🥳
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    DAXX.stop()
    print("𝐅𝐔𝐂𝐊𝐄𝐑 𝐍𝐀𝐊𝐒𝐇 𝐊𝐀 𝐁𝐄𝐓𝐀 𝐋𝐀𝐔𝐍𝐂𝐇 𝐇𝐎 𝐑𝐀 𝐇 𝐀𝐁 𝐓𝐎 𝐆𝐀𝐍𝐃 𝐌𝐀𝐑 𝐃𝐔𝐍𝐆𝐀 𝐒𝐁𝐊𝐈 𝐁𝐎𝐋𝐎 𝐁𝐎𝐒𝐒 𝗖𝗛𝗔𝗧𝗚𝗣𝗧 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣 !")
