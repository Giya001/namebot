import telebot
import requests
from telebot import types

token = ''

API = ''

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
  
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('GBP', callback_data='GBP'),
               types.InlineKeyboardButton('USD', callback_data='USD'),
               types.InlineKeyboardButton('RUB', callback_data='RUB'), )
    bot.send_message(message.chat.id, 'Choose your currency', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    querystring = {'from': call.data, 'to': 'UZS', 'amount': '1'}

    headers = {
        'X-RapidAPI-Key': '',
        'X-RapidAPI-Host': 'currency-converter-pro1.p.rapidapi.com',
    }

    response = requests.get(API, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        conversion_result = data['result']
        bot.send_message(call.message.chat.id, f'Conversion result :{conversion_result}')
    else:
        bot.send_message(call.message.chat.id, f'Failed to perform conversion. Please try again later.')


bot.polling()
