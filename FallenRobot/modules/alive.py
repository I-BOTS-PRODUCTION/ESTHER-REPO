import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
         "https://telegra.ph/file/27926d6cb3fa0e564b2b3.jpg",
         "https://telegra.ph/file/74807aeea259acbc97fa1.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
 TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ Ξ S Γ H Ξ Я​**\n━━━━━━━━━━━━━━━━━━━\n\n"
 TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝗤𝗨𝗥𝗘𝗦𝗛𝗜](https://t.me/BROTHER_OF_VILLAIN)** \n\n"
 TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
 TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
 TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
 BUTTON = [[Button.url("★ʜᴇʟᴘ★", "https://t.me/Missestherbot?start=help"), Button.url("★ꜱᴜᴘᴘᴏʀᴛ★", "https://t.me/ibotssupport")]]

ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)
