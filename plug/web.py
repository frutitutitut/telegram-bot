# import pyTelegramBotAPI, config, sleep
import telebot
from config import bot
import os
import urllib.request

def webcheck(m):
    sait = m.text
    if(sait != "/webcheck"):
        sait = sait.replace("/webcheck", '')
        sait = sait.replace(' ', '')
        sait = "https://" + sait
        print(sait)
        try:
            urllib.request.urlopen(sait)
            bot.send_message(m.chat.id, sait + " работает")
        except:
            bot.send_message(m.chat.id, sait + " не работает")
    else:
        bot.send_message(m.chat.id, "пусто")

def findip(m):
    web = m.text
    if(web != "/ipweb"):
        web = web.replace("/ipweb", "")
        print(web)
        ip = str(os.popen('ping -c1 ' + web).read())
        bracket1 = ip.find("(")
        bracket2 = ip.find(")")
        ip = ip[bracket1 + 1:bracket2]
        print(ip)
        bot.send_message(m.chat.id, 'Ip: ' + ip)
    else:
        bot.send_message(m.chat.id, 'пусто')

def scan(m):
    web = m.text
    if(web != "/webscanner"):
        web = web.replace("/webscanner", "")
        web = "https://www.shodan.io/host/" + web
        web = web.replace(' ', '')
        print(web)
        bot.send_message(m.chat.id, web)
    else:
        bot.send_message(m.chat.id, 'пусто')