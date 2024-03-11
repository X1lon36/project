import telebot
from time import sleep
bot = telebot.TeleBot('5654088447:AAGNsDUL7UJsdcWbaHKQzvmiVplBDGxp010')

@bot.message_handler(content_types=['text', 'audio'])

def text_messages(message):
    if message.text == "Привет":
        sleep(5)
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Хочу общения":
        sleep(6)
        bot.send_message(message.from_user.id, "Я тоже не против пообщаться")
    elif message.text == "Отлично":
        sleep(5)
        bot.send_message(message.from_user.id, "Начнёшь тему для общения?")
    elif message.text == "Чем занимаешься?":
        sleep(10)
        bot.send_message(message.from_user.id, "Я не могу чем-то заниматься кроме того как отвечать тебе")
    elif message.text == "Как тебя зовут?":
        sleep(7)
        bot.send_message(message.from_user.id, "я и сам не знаю, а тебя?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "привет \n хочу общения \n отлично \n чем занимаешься? \n как тебя зовут? ")
        


bot.polling(none_stop=True, interval=0)