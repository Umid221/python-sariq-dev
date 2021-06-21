from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '1771652376:AAEx2gx6jrkxGs0oKyLCUv15yrdV9mehLTA'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg) 
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()