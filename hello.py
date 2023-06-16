import telebot
import requests
bot = telebot.TeleBot('6215651953:AAHT_4kNGCbn4FYjWvdfuoaIoYED7JH4IgY')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text:

        response = requests.get('https://evilinsult.com/generate_insult.php?type=plain&lang=ru')
        print( message.text, message.from_user.username, response.text)
        if response.status_code == 200:
            insult = response.text
            bot.send_message(message.from_user.id, insult)
        else:
            bot.send_message(message.from_user.id, "Произошла ошибка при получении оскорбления. Попробуйте позже.")


bot.polling(none_stop=True, interval=0)
