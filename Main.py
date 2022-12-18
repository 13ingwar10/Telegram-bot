import telebot
from telebot import types
import Create_notebook
import csv

token = "5737846883:AAHpkd55saWsQhLzc7lRZuM_qotVS64hss8"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я бот-всезнайка. Чтобы узнать что-то новенькое, сначала зарегистрируйся')
    Create_notebook.create_list()

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Зарегистрироваться")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Приступим к регистрации:', reply_markup=markup)
    bot.register_next_step_handler(message, register_me)

@bot.message_handler(content_types=['text'])
def register_me(message):
    msg = bot.send_message(message.chat.id, 'Введите Имя')
    bot.register_next_step_handler(msg, enter_fio)

def enter_fio(message):
    new_user = []
    new_user.append(message.text)
    msg = bot.send_message(message.chat.id, 'Введите Фамилию')
    bot.register_next_step_handler(msg, enter_surname, new_user)

def enter_surname(message, new_user):
    new_user.append(message.text)
    msg = bot.send_message(message.chat.id, 'Введите номер телефона')
    bot.register_next_step_handler(msg, enter_tel, new_user)

def enter_tel(message, new_user):
    new_user.append(message.text)
    bot.send_message(message.chat.id, 'Регистрация завершена!')
    print(new_user)

bot.infinity_polling()
