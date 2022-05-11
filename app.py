import telebot
from config import TOKEN, values, main_menu, help
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['menu'])
def main_menuu(message):
    bot.send_message(message.chat.id, main_menu)

@bot.message_handler(commands=['start'])
def startt(message):
    bot.send_message(message.chat.id, help + '\n /menu')

@bot.message_handler(commands=['help'])
def helpp(message):
    bot.send_message(message.chat.id, help + '\n /menu')

@bot.message_handler(commands=['values'])
def valuess(message):
    bot.send_message(message.chat.id, 'ДОСТУПНЫ СЛЕДУЮЩИЕ ВАЛЮТЫ:')
    for i in values:
        bot.send_message(message.chat.id, i + ' ' + values[i] )
    bot.send_message(message.chat.id, '/menu')

@bot.message_handler(content_types=['text'])
def convert_result(message: telebot.types.Message):
    try:
        val = message.text.split(' ')

        if len(val) != 3:
            raise APIException('Слишком много или слишком мало параметров')

        base, quote, amount = val
        result = CryptoConverter.convert(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n {e}')
    else:
        text = f'{amount} {values[base]}({base}) в {values[quote]}({quote}) равно: {result}'
        bot.send_message(message.chat.id, text)
        bot.send_message(message.chat.id, "/menu")

bot.polling()



