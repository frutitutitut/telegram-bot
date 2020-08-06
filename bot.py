from plug.base64 import encoder, decoder
from config import bot, chat_id, user_id
from plug.web import webcheck, findip, scan
from plug.start import start, help, send_text
from plug.animals import cats, get_dogurl, dogs
from plug.chat import get_id, private_bot, id_chat
from plug.rate import eurorub, dollrub, btcrub, btcdoll, rate_dollar, rate_rub, rate_btc, rate_euro

# Start Bot
@bot.message_handler(commands=['start'])
def any_start(m):
    start(m)

# Help Bot
@bot.message_handler(commands=['help'])
def any_help(m):
    help(m)

# Get User ID
@bot.message_handler(commands=['id'])
def any_id(m):
    get_id(m)

# Get Chat ID
@bot.message_handler(commands=['chatid'])
def any_chatid(m):
    id_chat(m)

# Encode Text
@bot.message_handler(commands=['encode'])
def any_encode(m):
    encoder(m)

# Decode
@bot.message_handler(commands=['decode'])
def any_decode(m):
    decoder(m)

@bot.message_handler(commands=['webcheck'])
def any_webcheck(m):
    webcheck(m)

@bot.message_handler(commands=['ipweb'])
def any_ipweb(m):
    findip(m)

@bot.message_handler(commands=['webscanner'])
def any_webscanner(m):
    scan(m)

# Dollar to Ruble exchange rate
@bot.message_handler(commands=['dollar'])
def any_dollar(m):
    rate_dollar(m)
    
# Bitcoin to Ruble rate
@bot.message_handler(commands=['btcrub'])
def any_btcrub(m):
    rate_rub(m)

# Euro to Ruble exchange rate
@bot.message_handler(commands=['euro'])
def any_euro(m):
    rate_euro(m)

# Bitcoin to Dollar rate
@bot.message_handler(commands=['btcdoll'])
def any_btc(m):
    rate_btc(m)

@bot.message_handler(commands=['cats'])
def any_cats(m):
    cats(m)

@bot.message_handler(commands=['dogs']) # help message handler
def any_dogs(m):
    dogs(m)

@bot.message_handler(content_types=['text'])
def any_text(m):
    send_text(m)

# Start Bot
if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
