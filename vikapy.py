
import telebot

from config import API_TOKEN
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)


keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
button = KeyboardButton(text = "Налево",)
button2 = KeyboardButton(text = "Направо")
#button3 = KeyboardButton(text = "Моя кнопка 3")
keyboard.add(button)
keyboard.add(button2)


bot = telebot.TeleBot(API_TOKEN)

state = 0

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    bot.reply_to(message, f'YO YO YO GOOD MORNING {message.from_user.first_name} RISE AND GRIND!')
    bot.send_message (
        message.chat.id, 
        echo_message, 
        reply_markup=keyboard,
        parse_mode='HTML' 
    )
    state = 1

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global state
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, 'klV~', reply_markup=keyboard)
    if state == 1 and message.text == "Налево" :
        bot.send_message(
            message.chat.id,
            'Вы пошли налево во вторую комнату'
        )
        state = 2
    elif state == 1 and message.text == 'Haправo':
        bot.send_message(
            message.chat.id,
            'Вы пюшли направо в третью комнату' 
        )
        state = 3
    else:
        bot.send_message ( message. chat. id,
            'Вы нажали что-то не то'
        )
bot.infinity_polling()
