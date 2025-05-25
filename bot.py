import time, threading, schedule
from datetime import datetime
from telebot import TeleBot

API_TOKEN = '7671706348:AAEyY_86IyZM2OCEQ5PgkfHnjl17UCZpBhc'  # ⚠️ ЗАМЕНИ этот токен на новый!
bot = TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Use /set <seconds> to set a timer")


def beep(chat_id) -> None:
    bot.send_message(chat_id, text='Beep!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(str(message.chat.id))
        bot.reply_to(message, f'Будильник установлен через каждые {sec} секунд.')
    else:
        bot.reply_to(message, 'Usage: /set <seconds>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(str(message.chat.id))
    bot.reply_to(message, 'Будильник отключён.')

#новая функция
@bot.message_handler(commands=['time'])
def send_time(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    bot.reply_to(message, f"🕒 Время сейчас: {timestamp}")
    
if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
    while True:
        schedule.run_pending()
        time.sleep(1)




