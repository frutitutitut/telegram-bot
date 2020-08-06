# import pyTelegramBotAPI, config, sleep
import telebot
from config import bot
import base64

def encoder(m):
    message = m.text[7:]
    encode_message = message.encode()
    encode = base64.b64encode(encode_message)
    bot.send_message(m.chat.id, text=encode)

def decoder(m):
    message = m.text[7:]
    encode_message = message.encode()
    decode = base64.b64decode(encode_message)
    bot.send_message(m.chat.id, text=decode)