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
    if message.text == 'Зарегистрироваться':

        new_user = []
        for element in Create_notebook.list_header:
            bot.send_message(message.chat.id, f'Заполните поле {element}')
            bot.message_handler(content_types=['text'])
            bot.register_next_step_handler(message, fill_new_user)

            @bot.message_handler(content_types=['text'])
            def fill_new_user(message):
                new_user.append(message.text)


        # new_user = []
        # for element in Create_notebook.list_header:
        #     bot.send_message(message.chat.id, f'Заполните поле {element}')
        #     @bot.message_handler(content_types=['text'])
        #     def fill_new_user(message):
        #         new_user.append(message)
        # with open('notebook.csv', 'r') as f:
        #     writer = csv.writer(f, delimiter=';')
        #     writer.writerow(new_user)

bot.infinity_polling()
