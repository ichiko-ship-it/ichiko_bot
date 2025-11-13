
import telebot

from config import API_TOKEN
from telebot.types import (KeyboardButton,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove,
                           Message)


keyboard = ReplyKeyboardMarkup(row_width=2, resize_keyboard=False)
button = KeyboardButton(text = "Моя кнопка", request_location=True)
button2 = KeyboardButton(text = "Моя кнопка 2")
button3 = KeyboardButton(text = "Моя кнопка 3")
keyboard.add(button)
keyboard.add(button2)
keyboard.add(button3)

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    bot.reply_to(message, f'YO YO YO GOOD MORNING {message.from_user.first_name} RISE AND GRIND!')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    bot.send_message(message.chat.id, 'klV~', reply_markup=keyboard)


bot.infinity_polling()
