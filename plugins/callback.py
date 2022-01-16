import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from .commands import start, BATCH
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

@Client.on_callback_query(filters.regex('^help$'))
async def help_cb(c, m):
    await m.answer()

    # help text
    help_text = """**Yᴏᴜ ɴᴇᴇᴅ Hᴇʟᴘ?? 🧐**"""

    # creating buttons
    buttons = [[
            InlineKeyboardButton('Hᴏᴍᴇ 🏕', callback_data='home'),
            InlineKeyboardButton('Aʙᴏᴜᴛ 📕', callback_data='about')],[
            InlineKeyboardButton('Cʟᴏsᴇ 🔐', callback_data='close')
        ]]

    # editing as help message
    await m.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex('^close$'))
async def close_cb(c, m):
    await m.message.delete()
    await m.message.reply_to_message.delete()


@Client.on_callback_query(filters.regex('^about$'))
async def about_cb(c, m):
    await m.answer()
    owner = await c.get_users(int(OWNER_ID))
    bot = await c.get_me()

    # about text
#    about_text = f"""--**Mʏ Dᴇᴛᴀɪʟs:**--

#**⚜ Mʏ ɴᴀᴍᴇ : FɪʟᴇSᴛᴏʀᴇBᴏᴛ**\n
#**🔸Vᴇʀꜱɪᴏɴ :** `3.0.1`\n
#**🔹Sᴏᴜʀᴄᴇ :** [Cʟɪᴄᴋ Hᴇʀᴇ 🥰](https://github.com/avipatilpro/FileStoreBot)\n
#**🔸GitHub :** [Fᴏʟʟᴏᴡ](https://GitHub.com/avipatilpro)\n
#**🔹Dᴇᴠᴇʟᴏᴘᴇʀ :** [Aᴠɪsʜᴋᴀʀ Pᴀᴛɪʟ](https://telegram.me/Avishkarpatil)\n
#**🔸Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ :** [[ 11-ᴊᴜʟʏ-21 ] 04:35 PM](https://telegram.me/AvishkarPatil)
#"""

    about_text = f"""--**🍺 Mʏ Dᴇᴛᴀɪʟs:**--
    
╭───[ **🔅 FɪʟᴇSᴛᴏʀᴇBᴏᴛ 🔅** ]───⍟
│
├**🔸Vᴇʀꜱɪᴏɴ :** `3.0.1`
│
├**🔹Sᴏᴜʀᴄᴇ :** [Cʟɪᴄᴋ Hᴇʀᴇ 🥰](https://github.com/)
│
├**🔸GitHub :** [Fᴏʟʟᴏᴡ](https://GitHub.com/)
│
├**🔹Dᴇᴠᴇʟᴏᴘᴇʀ :** [Aᴠɪsʜᴋᴀʀ Pᴀᴛɪʟ](https://telegram.me/shreevish)
│
├**🔸Lᴀꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ :** [[ 𝟷𝟼-ᴊᴀɴ-𝟸𝟸 ]](https://telegram.me/shreevish)
│
╰─────────[ 😎 ]────────⍟
"""  

    # creating buttons
    buttons = [[
            InlineKeyboardButton('Hᴏᴍᴇ 🏕', callback_data='home'),
            InlineKeyboardButton('Hᴇʟᴘ 💡', callback_data='help')],[
            InlineKeyboardButton('Cʟᴏsᴇ 🔐', callback_data='close')
            ]]

    # editing message
    await m.message.edit(
        text=about_text,
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex('^home$'))
async def home_cb(c, m):
    await m.answer()
    await start(c, m, cb=True)


@Client.on_callback_query(filters.regex('^done$'))
async def done_cb(c, m):
    BATCH.remove(m.from_user.id)
    c.cancel_listener(m.from_user.id)
    await m.message.delete()


@Client.on_callback_query(filters.regex('^delete'))
async def delete_cb(c, m):
    await m.answer()
    cmd, msg_id = m.data.split("+")
    chat_id = m.from_user.id if not DB_CHANNEL_ID else int(DB_CHANNEL_ID)
    message = await c.get_messages(chat_id, int(msg_id))
    await message.delete()
    await m.message.edit("Dᴇʟᴇᴛᴇᴅ ғɪʟᴇs sᴜᴄᴄᴇssғᴜʟʟʏ Fʀᴏᴍ Dᴀᴛᴀʙᴀsᴇ👨‍✈️")
