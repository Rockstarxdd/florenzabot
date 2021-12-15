from telethon import events, Button, custom
import re, os
from innexiaBot.events import register
from innexiaBot import telethn as love
from innexiaBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/16bf7f2e7ca1543cb7694.jpg"
@register(pattern=("/alive"))
async def awake(event):
  LOVELY = event.sender.first_name
  LOVELY = "**❣️ I'm Working Properly ** \n\n"
  LOVELY += "**❣️ My Master : [Rockstar](t.me/Always_Rockstar) *\n\n"
  LOVELY += "**❣️ Library Version : `13.7` **\n\n"
  LOVELY += "**Telethon Version : `1.24.0` \n\n"
  LOVELY += "**Pyrogram Version : `1.2.20` \n\n"
  BUTTON = [[Button.url("𝗦𝗨𝗣𝗣𝗢𝗥𝗧🙂", "https://t.me/FlorenzaSupport"), Button.url("𝗨𝗣𝗗𝗔𝗧𝗘", "https://t.me/FlorenzaUpdates")]]
  await love.send_file(event.chat_id, PHOTO, caption=LOVELY,  buttons=BUTTON)
© 2021 GitHub, Inc.
