import telebot
from auth_data import token_telegram_bot
from telebot import types
import sqlite3


# conn = sqlite3.connect('DataBase.db', check_same_thread=False)
# cursor = conn.cursor()


# def db_table_val(user_id: int, user_name: str, user_surname: str):
# cursor.execute('INSERT INTO Telebot (user_id, user_name, user_surname) VALUES (?, ?, ?)',
# (user_id, user_name, user_surname))
# conn.commit()


def telegram_bot(token_telegram_bot):
    bot = telebot.TeleBot(token_telegram_bot)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Registration', 'Give number', 'All Good')
        msg = bot.reply_to(message, 'Hello', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)

    def process_step(message):
        chat_id = message.chat.id
        if message.text == 'Registration':
            msg = bot.send_message(message.chat.id, 'Input Your first and second Name')
            bot.register_next_step_handler(msg, name_message)

        if message.text == 'Give number':
            bot.send_message(message.chat.id, 'Які показники бажаєте подати ?')

    def name_message(message):
        FirstAndSecond_Name = message.text
        bot.send_message(message.chat.id, f'Перевірте Ваші данні: {FirstAndSecond_Name}')

    def give_address(message):
        if message.text == 'All Good':
            bot.send_message(message.chat.id, 'Input Your Address')

    bot.polling()


if __name__ == '__main__':
    telegram_bot(token_telegram_bot)
