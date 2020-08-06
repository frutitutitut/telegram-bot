# import pyTelegramBotAPI, config, sleep
import telebot
from config import bot
import re
import random
from time import sleep

def get_id(m):
    bot.send_chat_action(m.chat.id, 'typing') #тайпинг бота
    bot.send_message(m.chat.id, u"@" + str(m.from_user.username)+ ", " + "ваш Telegram ID: " + str(m.from_user.id))
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду

def private_bot(m):
    private = ['*Команда не работает в лс бота*', '*Команда работает только в чате*', '*Ну и зачем ты это делаешь?*']
    delete = bot.send_message(m.chat.id, " *!* " + random.choice(private) + " *!*", parse_mode="Markdown")
    sleep(5)
    bot.delete_message(m.chat.id, delete.message_id)

def id_chat(m):
    bot.send_chat_action(m.chat.id, 'typing') #тайпинг бота
    private = ['*Команда не работает в лс бота*', '*Команда работает только в чате*', '*Ну и зачем ты это делаешь?*']
    sleep(2)
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду
    status = ['creator', 'administrator', 'member']
    for chri in status:
        if chri == bot.get_chat_member(chat_id, user_id=m.from_user.id).status: #Проверить, находится ли пользователь в чате
            if m.chat.type == "private":
                private_bot(m)
            else:
                bot.send_message(m.chat.id, "Айди чата " + m.chat.title + ": " + str(m.chat.id), parse_mode="Markdown")