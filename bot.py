import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("8328643964:AAFQLAk4ADPWQZaZ0_w9B7R9WCYKKkAx_4Q")  # این خط توکن را از Environment Variable میخونه

def start(update, context):
    update.message.reply_text("ربات صرافی روشن شد ✔️")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
