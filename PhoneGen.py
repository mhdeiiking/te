import requests
from telebot import types
import telebot
from time import sleep
import random
import marshal  

token = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(token)

r=requests.session() 
co = types.InlineKeyboardButton(text ="- XDev", url="https://t.me/trprogram")



@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
Hi <code>{fr}</code>, 
- - - - - - - - - - 
Welcome To Number Generator
/get - To get New Number  & Automatically Send Receive Messages
- - - - - - - - - - 
By  : @trprogram 
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
@bot.message_handler(commands=['get'])
def com(message):
    url1 = requests.get("https://dev-khafer.pantheonsite.io/number.php?number=new").json()
    a = url1['result'][0]['number']
    s = url1['result'][0]['country']
    d = url1['result'][0]['update']
    bot.send_message(message.chat.id,f"<strong>Number : <code>{a}</code>\nCountry : {s}\nLast Update : {d}</strong>",parse_mode="html")
    sleep(1)
    while 1:
        sleep(15)
        url = requests.get(f"https://dev-khafer.pantheonsite.io/number.php?number=message&phone={a}").json()
        all1 = url['result'][0] ['message1']
        all2 = url['result'][0] ['message2']
        all3 = url['result'][0] ['message3']
        bot.send_message(message.chat.id,f"<strong>Message 1:\n- - - - - - - - - - - -\n{all1}\nMessage 2:\n- - - - - - - - - - - - \n{all2}\nMessage 3:\n- - - - - - - - - - - -\n{all3}</strong>",parse_mode="html")
        sleep(2)
        bot.send_message(message.chat.id,f"<strong>Send /get To See Messages! </strong>",parse_mode="html")
        pass    					             
bot.polling(True)