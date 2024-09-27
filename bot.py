import json
import telebot
from telebot import types
import random  
TOKEN = ''

bot = telebot.TeleBot(TOKEN)

# Пример списка анекдотов
jokes = [
    "Почему программисты не любят природу? Потому что в природе слишком много багов.",
    "Какой язык программирования не любят программисты? Молоко — потому что там много ошибок.",
    "Зачем программистам нужны сертификаты? Чтобы показать, что они могут ошибаться со статусом успеха!",]

with open('schedule.json', 'r', encoding='utf-8') as f:
    schedule = json.load(f)

def display_schedule():
    text = "Расписание уроков: \n"
    for day in schedule:
        text += f"{day['day']} \n"
        for lesson in day['lessons']:
            text += f"- {lesson['time']}: {lesson['subject']} \n"
        text += "\n"
    return text

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    schedule_button = types.KeyboardButton("Расписание уроков")
    info_button = types.KeyboardButton("Информация")
    joke_button = types.KeyboardButton("anekdot")  # Добавляем кнопку "anekdot"

    keyboard.add(schedule_button, info_button, joke_button)
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите опцию:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Расписание уроков":
        bot.send_message(message.chat.id, display_schedule())
    elif message.text == "Информация":
        info_message = (
            "Я бот, который может помочь вам:\n"
            "- Показать расписание уроков\n"
            "- Ответить на ваши вопросы\n"
            "- Обеспечить дополнительные ресурсы и материалы\n"
            "Просто выберите нужную опцию!"
        )
        bot.send_message(message.chat.id, info_message)
    elif message.text == "anekdot":  # Обработка нажатия кнопки "anekdot"
        joke = random.choice(jokes)  # Случайный выбор анекдота
        bot.send_message(message.chat.id, joke)

bot.polling(none_stop=True)
