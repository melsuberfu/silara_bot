import os
import telebot
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Hello, I am Silara. How can I help you?")

bot.polling()
