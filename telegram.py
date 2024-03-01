import telebot
from io import StringIO
import sys
import os
import subprocess
from subprocess import Popen, PIPE
import config
from ctypes import *
import pyautogui
import datetime
from pymsgbox import *
from PIL import ImageGrab

from telebot import types

    
bot = telebot.TeleBot(config.TOKEN)

aut = []


@bot.message_handler(commands=['srt'])
def welcome(message):
    bot.send_message(message.chat.id, "Введите пароль :",
        parse_mode='html')
    bot.register_next_step_handler(message, lala)


@bot.message_handler(commands=['login'])
def lala(message):
    try:
        user1 = message.text.split(" ")[1]
        password = ("12345")
        if user1 != password:
            bot.send_message(message.chat.id, "❌ Ошибка: пароль не верный")
            bot.register_next_step_handler(message, lala)
        if user1 == password:
            aut.append(message.from_user.id)
            bot.send_message(message.chat.id, "✅ Вход успешен")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("🌅 Сделать скриншот")
            item2 = types.KeyboardButton("🛑 Выключение компьютера")
            item3 = types.KeyboardButton("❕ Уведомление")
            item4 = types.KeyboardButton("🔐 Заблокировать компьютер")
            item5 = types.KeyboardButton("⭕️ Перезагрузка компьютера")
            item6 = types.KeyboardButton("🛠 Диспетчер задач")
            item7 = types.KeyboardButton("⤵️ Назад")
            markup.add(item1,item2,item3,item4,item5,item6,item7)
            bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name} 😄\nПанель управлениея :".format(message.from_user, bot.get_me()),
            parse_mode='html', reply_markup=markup)
            bot.register_next_step_handler(message, la123)
    except Exception as ex:
        bot.send_message(message.chat.id, "❌ Ошибка: пароль не верный")



@bot.callback_query_handler(func=lambda call: True)
def reg_soobje(message):
    if message.text == '⤵️ Назад':
        bot.register_next_step_handler(message, la123)
        bot.send_message(message.chat.id, "❌ Дейвстивие отменено")
    else:
        soob = message.text
        alert(text=soob, title="Уведомление", button='OK')
        bot.send_message(message.chat.id, "✅ Успешно")
        bot.register_next_step_handler(message, la123)
def reg_soob(message):
    if message.text == '⤵️ Назад':
        bot.register_next_step_handler(message, la123)
        bot.send_message(message.chat.id, "❌ Отмена")
    else:  
        bob = message.text
        os.system("taskkill /im "+ bob + (".exe"))
        bot.send_message(message.chat.id, "✅ Успешно")
        bot.register_next_step_handler(message, reg_soob)


@bot.message_handler(content_types=['text'])
def la123(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.chat.type == 'private' and message.from_user.id in aut: 
        if message.text == '🌅 Сделать скриншот':
            im2 = ImageGrab.grab()
            filename = 'screenshot_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.png'
            im2.save(filename)
            p = open(filename, 'rb')
            bot.send_photo(message.chat.id, p)
            bot.send_message(message.chat.id, "✅ Успешно", reply_markup=markup)
        elif message.text == '🛑 Выключение компьютера':
            os.system('shutdown -s')
            bot.send_message(message.chat.id, "✅ Успешно")
        elif message.text == '⭕️ Перезагрузка компьютера':
            os.system( "shutdown /s" )
            bot.send_message(message.chat.id, "✅ Успешно")
        elif message.text == '❕ Уведомление':
            bot.send_message(message.chat.id, "Введите сообщение :")
            bot.register_next_step_handler(message, reg_soobje)
        elif message.text == '🔐 Заблокировать компьютер':
            user32=windll.LoadLibrary('user32.dll')
            user32.LockWorkStation()
            bot.send_message(message.chat.id, "✅ Успешно")
        elif message.text == '🛠 Диспетчер задач':
            bot.send_message(message.chat.id, "Какой процес закрыть :")
            bot.register_next_step_handler(message, reg_soob)
        elif message.text == '⤵️ Назад':
            bot.send_message(message.chat.id, "✅ Успешно")
        else:
            bot.send_message(message.chat.id, 'Нет такой комманды')
    else:
        bot.send_message(message.chat.id, '❌ Вы не авторизованны! \nДля авторизации введите: /login "пароль"')
# RUN
bot.polling(none_stop=True)