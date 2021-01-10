from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

def start(update, context):
    user = update.message.from_user
    buttons = [[
        InlineKeyboardButton('Qo\'qon', callback_data='region_1'),
        InlineKeyboardButton('Andijon', callback_data='region_2')
        ]]

    update.message.reply_html('Assalamu alaykum <b>{}!</b>\n \n<i>Ramazon oyi muborak bo\'lsin</i>\n \nSizga qaysi mintaqa bo\'yicha malumot beraylik?'.
    format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))

def main():
    # Updaterni o'rnatib olamiz
    updater = Updater('Token10', use_context=True)

    # Dispatcherni eventlarini aniqlash uchun
    dispatcher = updater.dispatcher

    # start kommandasini ushlab qolish
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

main()
