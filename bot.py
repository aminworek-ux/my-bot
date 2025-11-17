import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = "8328643964:AAFQLAk4ADPWQZaZ0_w9B7R9WCYKKkAx_4Q
"

def start(update, context):
    update.message.reply_text("ربات صرافی روشن شد ✔️")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
