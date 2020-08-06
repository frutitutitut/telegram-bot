# import pyTelegramBotAPI, config, sleep
import telebot
import requests
from config import bot
from bs4 import BeautifulSoup
from parsing import dollar_rub, btc_rub, euro_rub, btc_dollar, headers

def cats(m):
    bot.delete_message(m.chat.id, m.message_id)
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    search = "https://theoldreader.com/kittens/1366/768/js"
    url = requests.get(search, headers=user_agent) #Делаем запрос
    soup = BeautifulSoup(url.text, features="lxml") #Получаем запрос
    result = soup.find("img").get("src") #Ищем тег <img src="ссылка.png"
    result = "https://theoldreader.com" + result
    bot.send_photo(m.chat.id,photo=result, parse_mode= "Markdown")

# retrieve dog photo from the api
def get_dogurl():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def dogs(m):
    url = get_dogurl()
    bot.delete_message(m.chat.id, m.message_id)
    bot.send_photo(m.chat.id, photo=url)