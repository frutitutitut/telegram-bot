# import pyTelegramBotAPI, config, sleep
import telebot
from config import bot

# /start
def start(m):
    bot.send_chat_action(m.chat.id, 'typing') # typing bot
    bot.send_message(m.chat.id, 'Hello,  ' u"@" + str(m.from_user.username) + ' ! ')
    bot.delete_message(m.chat.id, m.message_id) # delete /start command

def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Приветствую, выполни команду /help и познаешь всю мою мощь')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорой встречи, до скооороойй встречиии')

# /help
def help(m):
    bot.send_chat_action(m.chat.id, 'typing') # typing bot
    bot.send_message(m.chat.id, '\n/webcheck *( Website address )* - _Checking the site_'
                                '\n/ipweb *( Website address )* - _Find out the IP of the server on which the site is located_'
                                '\n/webscanner *( IP )* - _Show information about IP, as well as vulnerabilities ( if any )_'
                                '\n/id _- Get my ID_'
                                '\n/chatid _- Get chat ID_'
                                '\n/euro _- Show EUR to RUB rate_'
                                '\n/dollar _- Show dollar exchange rate in rubles_'
                                '\n/btcrub _- Show bitcoin rate in rubles_'
                                '\n/btcdoll _- Show bitcoin rate in dollars_'
                                '\n/encode *( Text )* - _Encode text in base64_'
                                '\n/decode *( Cipher text )* - _Decode text from base64_'
                                '\n/cats _- Send a cat_'
                                '\n/dogs _- Send a dog_', parse_mode="Markdown")
    bot.delete_message(m.chat.id, m.message_id) # delete /help command
