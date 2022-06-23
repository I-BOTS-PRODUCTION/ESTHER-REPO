import os
import html
import nekos
import requests
from PIL import Image
from telegram import ParseMode
from FallenRobot import dispatcher, updater
import FallenRobot.modules.sql.nsfw_sql as sql
from FallenRobot.modules.log_channel import gloggable
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CommandHandler, run_async, CallbackContext
from FallenRobot.modules.helper_funcs.filters import CustomFilters
from FallenRobot.modules.helper_funcs.chat_status import user_admin
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown

@run_async
@user_admin
@gloggable
def add_nsfw(update: Update, context: CallbackContext):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user #Remodified by @EverythingSuckz
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        sql.set_nsfw(chat.id)
        msg.reply_text("ɴsғᴡ ᴍᴏᴅᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ !")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ ɴsғᴡ ᴍᴏᴅᴇ\n"
            f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message
    else:
        msg.reply_text("ɴsғᴡ ᴍᴏᴅᴇ ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ !")
        return ""


@run_async
@user_admin
@gloggable
def rem_nsfw(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        msg.reply_text("ɴsғᴡ ᴍᴏᴅᴇ ᴀʟʀᴇᴀᴅʏ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ")
        return ""
    else:
        sql.rem_nsfw(chat.id)
        msg.reply_text("ʙᴀᴄᴋ ᴛᴏ sғᴡ ᴍᴏᴅᴇ !")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ ɴsғᴡ\n"
            f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message

@run_async
def list_nsfw_chats(update: Update, context: CallbackContext):
    chats = sql.get_all_nsfw_chats()
    text = "<b>NSFW Activated Chats</b>\n"
    for chat in chats:
        try:
            x = context.bot.get_chat(int(*chat))
            name = x.title if x.title else x.first_name
            text += f"• <code>{name}</code>\n"
        except BadRequest:
            sql.rem_nsfw(*chat)
        except Unauthorized:
            sql.rem_nsfw(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")



ADD_NSFW_HANDLER = CommandHandler("addnsfw", add_nsfw)
REMOVE_NSFW_HANDLER = CommandHandler("rmnsfw", rem_nsfw)
LIST_NSFW_CHATS_HANDLER = CommandHandler(
    "nsfwchats", list_nsfw_chats, filters=CustomFilters.dev_filter)


dispatcher.add_handler(ADD_NSFW_HANDLER)
dispatcher.add_handler(REMOVE_NSFW_HANDLER)
dispatcher.add_handler(LIST_NSFW_CHATS_HANDLER)


__handlers__ = [
    ADD_NSFW_HANDLER,
    REMOVE_NSFW_HANDLER,
    LIST_NSFW_CHATS_HANDLER,
    
]


__help__ = """
*NSFW:*
/addnsfw : Enable NSFW mode
/rmnsfw : Disable NSFW mode
"""

__mod_name__ = "Nsғᴡ"
