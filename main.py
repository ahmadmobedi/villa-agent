import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
    ["🏡 املاک", "📈 بورس ایران"],
    ["🥇 صندوق‌های طلا", "🌍 فارکس"],
    ["🤖 چت با هوش مصنوعی", "⚙️ تنظیمات"]
]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
    "سلام احمد 👋\nبه ربات اختصاصی احمد موبدی خوش آمدی.",
    reply_markup=reply_markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
دستورات ربات

/start
شروع ربات

/help
نمایش راهنما
"""
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📈 بورس ایران":
        await update.message.reply_text("بخش بورس ایران به زودی فعال می‌شود.")

    elif text == "🥇 صندوق‌های طلا":
        await update.message.reply_text("بخش صندوق‌های طلا به زودی فعال می‌شود.")

    elif text == "🌍 فارکس":
        await update.message.reply_text("بخش فارکس به زودی فعال می‌شود.")

    elif text == "🏡 املاک":
        await update.message.reply_text("بخش املاک به زودی فعال می‌شود.")

    elif text == "🤖 چت با هوش مصنوعی":
        await update.message.reply_text("هوش مصنوعی به زودی متصل می‌شود.")

    elif text == "⚙️ تنظیمات":
        await update.message.reply_text("بخش تنظیمات به زودی اضافه می‌شود.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
