
import telebot

from config import API_TOKEN
from telebot.types import Message
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)


keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = telebot.types.KeyboardButton(text="1")
button2 = telebot.types.KeyboardButton(text="2")
button3 = telebot.types.KeyboardButton(text="3")
button4 = telebot.types.KeyboardButton(text="4")
button5 = telebot.types.KeyboardButton(text="5")
button6 = telebot.types.KeyboardButton(text="6")
keyboard.add('1', '2', '3', '4', '5', '6')


bot = telebot.TeleBot(API_TOKEN)

state = 0

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    bot.reply_to(message, f'YO YO YO GOOD MORNING {message.from_user.first_name} RISE AND GRIND!')
    bot.send_message (
        message.chat.id, 
        'text_message', 
        reply_markup=keyboard,
        parse_mode='HTML' 
    )
    state = 1

@bot.message_handler(func=lambda message: True)
def text_message(message):
    global state
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboard)
    if state == 1 and message.text == "1" :
        bot.send_message(
            message.chat.id,
            'Вы пошли налево во вторую комнату'
        )
        state = 2
    elif state == 1 and message.text == '2':
        bot.send_message(
            message.chat.id,
            'Вы пошли направо в третью комнату' 
        )
        state = 3
    elif state == 2 and message.text == '3':
        bot.send_message(
            message.chat.id,
            'Вы пошли налево в четвертую комнату'
        )
        state = 4
    elif state == 3 and message.text == '4':
        bot.send_message(
            message.chat.id,
            'Вы пошли направо в шестую комнату'
        )
        state = 6
    elif state == 2 and message.text == '5':
        bot.send_message(
            message.chat.id,
            'Вы пошли направо в пятую комнату'
        )
        state = 5
    elif state == 3 and message.text == '6':
        bot.send_message(
            message.chat.id,
            'Вы пошли налево в пятую комнату'
        )
        state = 5
    else:
        bot.send_message ( message. chat. id,
            'Вы нажали что-то не то'
        )
bot.infinity_polling()
