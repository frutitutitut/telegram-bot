# import pyTelegramBotAPI, config, sleep
import telebot
import requests
from config import bot
from bs4 import BeautifulSoup
from parsing import dollar_rub, btc_rub, euro_rub, btc_dollar, headers

def eurorub():
    full_page = requests.get(euro_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

def dollrub():
    full_page = requests.get(dollar_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

def btcrub():
    full_page = requests.get(btc_rub, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

def btcdoll():
    full_page = requests.get(btc_dollar, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    return convert[0].text

def rate_dollar(m):
    bot.send_message(m.chat.id, "курс доллара к рублю: " + dollrub() + "Р")
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду

def rate_rub(m):
    bot.send_message(m.chat.id, "курс биткоина к рублю: " + btcrub() + "Р")
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду

def rate_euro(m):
    bot.send_message(m.chat.id, "курс евро к рублю: " + eurorub() + "Р")
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду

def rate_btc(m):
    bot.send_message(m.chat.id, "курс биткоина к доллару: " + btcdoll() + "$")
    bot.delete_message(m.chat.id, m.message_id) #Удалить сообщение, содержащее команду