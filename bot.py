import os
from telebot import TeleBot, types

bot = TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    watch_button = types.InlineKeyboardButton("ابدأ ", url="http://t.me/spor7bot/sport")
    markup.add(watch_button)
    
    bot.send_message(message.chat.id, "مرحباً! انقر على الزر أدناه لبدء مشاهدة المباريات:", reply_markup=markup)

bot.polling()
