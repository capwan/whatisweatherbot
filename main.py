import pyowm
import telebot
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('c19ac12a384b37dd79f6408bf1560726', config_dict)
bot = telebot.TeleBot("1763102450:AAG8R7etHjR14_7Gb_BfHIrs1l3ek2gnSbM")

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привет 🤚🏻 {message.from_user.first_name}! </b>\nКакой город тебя интересует?🌍"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    try :
         mgr = owm.weather_manager()
         observation = mgr.weather_at_place(message.text)
         w = observation.weather
         #print(w.wind()['speed'], w.temperature('celsius')['temp'])
         weather_info = "🏫 В городе "+message.text+" сейчас "+w.detailed_status+"\n"
         weather_info += "☀️ Температура: " + str(w.temperature('celsius')['temp']) + "\n"
         weather_info += "🔼 Максимальная температура: " +str(w.temperature('celsius')['temp_max']) + "\n"
         weather_info += "🔽 Минимальная температура: " +str(w.temperature('celsius')['temp_min']) + "\n"
         weather_info += "💨 Скорость ветра: " + str(w.wind()['speed']) + " м/с" + "\n"
         weather_info += "🌕 Восход солнца: " + str(w.sunrise_time(timeformat='iso')) + "\n"
         weather_info += "🌑 Заход солнца: " + str(w.sunset_time(timeformat='iso')) + "\n"
         weather_info += "Влажность: " + str(w.humidity(int)) + "\n"
         


         bot.reply_to(message, weather_info)
    except:
         error = f"<b> Данный город не найден. </b>"
         bot.send_message(message.chat.id, error, parse_mode='html')     



bot.polling(none_stop=True)
