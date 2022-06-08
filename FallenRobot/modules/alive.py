import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = "https://te.legra.ph/file/e56ca14f024117b4f8e4f.jpg"

@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ Ξ S Γ H Ξ Я​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝗤𝗨𝗥𝗘𝗦𝗛𝗜](https://t.me/BROTHER_OF_VILLAIN)** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/MissEstherBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/ibotssupport")]]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)


## Alive mod
