from telebot import types

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                      one_time_keyboard=True,
                                      row_width=2)
button1 = types.KeyboardButton(text='Поточні курси 🕰 📊')
button2 = types.KeyboardButton(text='Обміняти валюту 🔁')
main_menu.add(button1, button2)

exchange_choose_menu = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                 one_time_keyboard=True,
                                                 row_width=2)
button3 = types.KeyboardButton(text='Гривня 🇺🇦')
button4 = types.KeyboardButton(text='Іноземні 🇺🇳')
exchange_choose_menu.add(button3, button4)

rate_menu = types.InlineKeyboardMarkup(row_width=2)
key1 = types.InlineKeyboardButton(text='Курс Долара 🇺🇸', callback_data='USD_rate')
key2 = types.InlineKeyboardButton(text='Курс Евро 🇪🇺', callback_data='EUR_rate')
rate_menu.add(key1, key2)

exchange_menu1 = types.InlineKeyboardMarkup(row_width=2)
key3 = types.InlineKeyboardButton(text='USD 🇺🇸 🔁 UAH 🇺🇦', callback_data='USD_to_UAH')
key4 = types.InlineKeyboardButton(text='EUR 🇪🇺 🔁 UAH 🇺🇦', callback_data='EUR_to_UAH')
exchange_menu1.add(key3, key4)

exchange_menu2 = types.InlineKeyboardMarkup(row_width=2)
key5 = types.InlineKeyboardButton(text='UAH 🇺🇦 🔁 USD 🇺🇸', callback_data='UAH_to_USD')
key6 = types.InlineKeyboardButton(text='UAH 🇺🇦 🔁 EUR 🇪🇺', callback_data='UAH_to_EUR')
exchange_menu2.add(key5, key6)
