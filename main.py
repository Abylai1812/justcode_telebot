import telebot
from env import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Привет! Я бот созданный для работы ученика группы Python-16 Тогамысов Абулхаиром")

bot.polling()
