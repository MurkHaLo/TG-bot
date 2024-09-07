import json
import telebot

# Создание бота
bot = telebot.TeleBot(TOKEN)

# Загрузка расписания уроков
with open('schedule.json', 'r') as f:
    schedule = json.load(f)

# Функция для вывода расписания уроков
def display_schedule():
    text = "Расписание уроков:\n\n"
    for day in schedule:
        text += f"{day['day']}\n"
        for lesson in day['lessons']:
            text += f"- {lesson['time']}: {lesson['subject']}\n"
        text += "\n"
    return text

# Функция для обработки кнопок
def handle_buttons(message):
    if message.text == "Расписание уроков":
        bot.send_message(message.chat.id, display_schedule())

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Привет! Я Tvoi Bro. Что тебе нужно?")
        bot.send_message(message.chat.id, "Расписание уроков", reply_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add(telebot.types.KeyboardButton("Расписание уроков")))
    else:
        handle_buttons(message)

# Обработчик кнопок
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "schedule":
        bot.send_message(call.message.chat.id, display_schedule())

# Запуск бота
bot.polling()
