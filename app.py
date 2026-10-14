import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

WELCOME = """
⚡ BATTHARIHARI AI TECH-க்கு வணக்கம் நண்பா! ⚡

🔋 நான் உங்க Battery AI Assistant!

/start - Menu பார்க்க
உங்க Vehicle Model அனுப்புங்க, Best Price சொல்றேன்!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [
        [InlineKeyboardButton("🔋 Price List", callback_data='price')],
        [InlineKeyboardButton("🛠️ Service", callback_data='service')],
        [InlineKeyboardButton("📍 Location", callback_data='loc')],
        [InlineKeyboardButton("📞 Contact", callback_data='contact')]
    ]
    await update.message.reply_text(WELCOME, reply_markup=InlineKeyboardMarkup(kb))

async def btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == 'price':
        await q.edit_message_text("🔋 Price:\nBike Rs.1200+\nCar Rs.3500+\nAuto Rs.2500+\nInverter Rs.8000+")
    elif q.data == 'service':
        await q.edit_message_text("🛠️ Free Fitting, Free Checkup, Old Battery Exchange Available!")
    elif q.data == 'loc':
        await q.edit_message_text("📍 BATTHARIHARI AI TECH - Chennai")
    else:
        await q.edit_message_text("📞 Contact: +91 9XXXXXXXXX")

async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Super நண்பா! {update.message.text} க்கு Best Battery இருக்கு! /start தட்டுங்க!")

def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN Missing!")
        return
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(btn))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, msg))
    print("Bot Running...")
    app.run_polling()

if __name__ == '__main__':
    main()
