from tokenize import Token
from transliterate import to_cyrillic, to_latin
import telebot


Token = '5315774589:AAHqy54MCOhTNm8n9B77LTOeFYlfUgpYB9c'
bot = telebot.TeleBot(Token, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, javob)
    javob = message, "Assalomu alaykum, xush kelibsiz"
    javob += "\nMatn kiriting:"
    
    bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinty_polling()

