import telebot

bot = telebot.TeleBot("6772838394:AAHLkIxyUFllSS81hmV3jAKkNq0aRuEfqA0")

first_button = telebot.types.InlineKeyboardButton("Owner", url="https://t.me/Nerdcyber")
second_button = telebot.types.InlineKeyboardButton("Channel", url="https://t.me/cyber_guide")
markup = telebot.types.InlineKeyboardMarkup(row_width=2)
markup.add(first_button, second_button)

test_callback = telebot.types.InlineKeyboardButton("test", url="")
callback_button = telebot.types.InlineKeyboardButton("Callback data", callback_data="Hi")
callback_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
callback_markup.add(test_callback, callback_button)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.send_message(call.message.chat.id, "You clicked on Hi button")

@bot.message_handler(commands=["start"])
def send_welcome(messagee):
    bot.send_message(messagee.chat.id, "Hi", reply_markup=markup)

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
key_markup.add("One", "Two", "Three")


@bot.message_handler(commands=["help"])
def help_me(message):
    bot.reply_to(message, "What can I do?", reply_markup=key_markup)

@bot.message_handler()
def keyboard(message):
    if message.text == "One":
        bot.send_message(message.chat.id, "You tappen on One button...")
    elif message.text == "Two":
        bot.send_message(message.chat.id, "You tapped on Two button...")
    elif message.text == "Three":
        bot.send_message(message.chat.id, "You tapped on Three button...")


@bot.message_handler(commands=["custom"])
def callback_button(message):
    bot.send_message(message.chat.id, "This is for callback data test", reply_markup=callback_markup)



bot.infinity_polling()