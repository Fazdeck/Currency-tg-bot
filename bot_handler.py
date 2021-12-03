import telebot
from keyboard import *
from data import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(chat_id=message.chat.id,
                     text=f'*Вітаю, {message.from_user.first_name}*',
                     reply_markup=main_menu
                     )


@bot.message_handler(content_types=['text'])
def show_rates(message):
    if message.text == 'Поточні курси 🕰 📊':
        bot.send_message(chat_id=message.chat.id,
                         text='💵Оберіть валюту💶',
                         reply_markup=rate_menu)
    elif message.text == 'Обміняти валюту 🔁':
        bot.send_message(chat_id=message.chat.id,
                         text='Яку саме?',
                         reply_markup=exchange_choose_menu)
    elif message.text == 'Гривня 🇺🇦':
        bot.send_message(chat_id=message.chat.id,
                         text = 'Оберіть:',
                         reply_markup=exchange_menu2)
    elif message.text == 'Іноземні 🇺🇳':
        bot.send_message(chat_id=message.chat.id,
                         text = 'Оберіть:',
                         reply_markup=exchange_menu1)
    else:
        bot.send_message(chat_id=message.chat.id,
                         text='Команди не існує!⛔️',
                         reply_markup=main_menu)


@bot.callback_query_handler(func=lambda call: call.data == 'USD_rate')
def get_usd_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                     message_id=call.message.id,
                     text=f'Курс продажу*{USD_buy}*\nКурс купівлі *{USD_sale}',
                     parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'EUR_rate')
def get_eur_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                     message_id=call.message.id,
                     text=f'Курс продажу*{EUR_buy}*\nКурс купівлі *{EUR_sale}',
                     parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'RUB_rate')
def get_rub_rate(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                     message_id=call.message.id,
                     text=f'Курс продажу*{RUB_buy}*\nКурс купівлі *{RUB_sale}',
                     parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'UAH_to_USD')
def get_uah_to_usd(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                     message_id=call.message.id,
                     text='Введіть суму у гривнях: ')
    bot.register_next_step_handler(message=msg, callback=get_uah_to_usd)

def uah_to_usd(msg):
    try:
        uah = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {uah} ₴ можете купити {round(uah/USD_sale, 2)} $')
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Ви не ввели суму. Спробуйте ще!')
        bot.register_next_step_handler(message=msg, callback=get_uah_to_usd)


@bot.callback_query_handler(func=lambda call: call.data == 'USD_to_UAH')
def get_usd_to_uah(call):
    msg = bot.edit_message_text(chat_id=call.message.id,
                     message_id=call.message.id,
                     text='Введіть суму у доларах США: ')
    bot.register_next_step_handler(message=msg, callback=get_uah_to_usd)


def usd_to_uah(msg):
    try:
        usd = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {usd} $ можете купити {round(USD_buy*usd, 2)} ₴')
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Ви не ввели суму. Спробуйте ще!')
        bot.register_next_step_handler(message=msg, callback=get_usd_to_uah)


@bot.callback_query_handler(func=lambda call: call.data == 'EUR_to_UAH')
def get_eur_to_uah(call):
    msg = bot.edit_message_text(chat_id=call.message.id,
                     message_id=call.message.id,
                     text='Введіть суму у евро: ')
    bot.register_next_step_handler(message=msg, callback=get_eur_to_uah)


def eur_to_uah(msg):
    try:
        eur = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {eur} € можете купити {round(EUR_buy*eur, 2)} ₴')
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Ви не ввели суму. Спробуйте ще!')
        bot.register_next_step_handler(message=msg, callback=get_eur_to_uah)


@bot.callback_query_handler(func=lambda call: call.data == 'UAH_to_EUR')
def get_uah_to_eur(call):
    msg = bot.edit_message_text(chat_id=call.message.id,
                     message_id=call.message.id,
                     text='Введіть суму у гривнях: ')
    bot.register_next_step_handler(message=msg, callback=get_uah_to_eur)


def uah_to_eur(msg):
    try:
        uah = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {uah} ₴ можете купити {round(uah/EUR_sale,2)} €')
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Ви не ввели суму. Спробуйте ще!')
        bot.register_next_step_handler(message=msg, callback=get_uah_to_eur)


@bot.callback_query_handler(func=lambda call: call.data == 'UAH_to_RUB')
def get_uah_to_rub(call):
    msg = bot.edit_message_text(chat_id=call.message.id,
                     message_id=call.message.id,
                     text='Введіть суму у гривнях: ')
    bot.register_next_step_handler(message=msg, callback=get_uah_to_rub)


def uan_to_rub(msg):
    try:
        uah = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {uah} ₴ можете купити {round(uah/RUB_sale, 2)} ₽')
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Ви не ввели суму. Спробуйте ще!')
        bot.register_next_step_handler(message=msg, callback=get_uah_to_rub)


@bot.callback_query_handler(func=lambda call: call.data == 'RUB_to_UAH')
def get_rub_to_uah(call):
    msg = bot.edit_message_text(chat_id=call.message.id,
                     message_id=call.message.id,
                     text='Введіть суму у рублях: ')
    bot.register_next_step_handler(message=msg, callback=get_rub_to_uah)


def rub_to_uah(msg):
    try:
        rub = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {rub} ₽ можете купити {round(RUB_buy*rub, 2)} ₴')
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Ви не ввели суму. Спробуйте ще!')
        bot.register_next_step_handler(message=msg, callback=get_rub_to_uah)


