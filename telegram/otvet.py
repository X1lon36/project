def text_messages(message):   
    if message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "хочу общения":
        bot.send_message(message.from_user.id, "Я тоже не против пообщаться")
    elif message.text == "отлично":
        bot.send_message(message.from_user.id, "Начнёшь тему для общения?")
    elif message.text == "чем занимаешься?":
        bot.send_message(message.from_user.id, "Я не могу чем-то заниматься кроме того как отвечать тебе")
    elif message.text == "как тебя зовут?":
        bot.send_message(message.from_user.id, "я и сам не знаю")