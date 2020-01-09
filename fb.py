import telebot

#main variables
TOKEN = '1039762282:AAFdXTIqnecH4xT3ma9-eaxnnaqvi0Ifosc'
bot = telebot.TeleBot(TOKEN)

#handlers
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    if message.text == "Прривет":
        bot.send_message(message.from_user.id, "Пуривет")
    elif message.text == "Кто ты?":
        bot.send_message(message.from_user.id, "Я тестовый чатбот для учебного примера.")
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.from_user.id, "Меня зовут MyFirstTestBot.")
    elif message.text == "Что ты умеешь?":
        bot.send_message(message.from_user.id, "Я умею отвечать на несколько простых вопросов - кто я, как меня зовут и что я умею делать.")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши что-то другое.")
        
# bot.polling(none_stop=True, interval=0)
