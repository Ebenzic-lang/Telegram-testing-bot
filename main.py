import telebot
import os

BOT_TOKEN = os.getenv("8734287473:AAHioLxH6YK3l8SEDugaIY2qxjRhZMplUtQ")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Your bot is live 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
