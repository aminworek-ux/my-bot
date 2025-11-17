import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("TOKEN")  # این خط توکن را از Environment Variable میخونه

def start(update, context):
    update.message.reply_text("ربات صرافی روشن شد ✔️")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
