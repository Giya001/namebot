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


