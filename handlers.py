from telegram import Update
from telegram.ext import ContextTypes

from menus import (
    main_menu,
    real_estate_menu,
    market_analysis_menu,
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "سلام احمد 👋\nبه ربات اختصاصی احمد موبدی خوش آمدی.",
        reply_markup=main_menu()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
"""
/start
شروع ربات

/help
راهنما
"""
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "🏡 املاک":

        await update.message.reply_text(
            "🏡 بخش املاک",
            reply_markup=real_estate_menu()
        )

    elif text == "🔙 بازگشت":

        await update.message.reply_text(
            "منوی اصلی",
            reply_markup=main_menu()
        )

    elif text == "🏠 ثبت ملک":

        await update.message.reply_text(
            "ثبت ملک به زودی فعال می‌شود."
        )

    elif text == "🔍 جستجوی ملک":

        await update.message.reply_text(
            "جستجوی ملک به زودی فعال می‌شود."
        )

    elif text == "📋 فایل‌های من":

        await update.message.reply_text(
            "فایل‌های شما نمایش داده خواهد شد."
        )

    elif text == "❤️ علاقه‌مندی‌ها":

        await update.message.reply_text(
            "علاقه‌مندی‌ها به زودی فعال می‌شود."
        )

    elif text == "📊 تحلیل بازار":

        await update.message.reply_text(
        "📊 تحلیل بازار املاک",
        reply_markup=market_analysis_menu()
        )

    elif text == "🔙 بازگشت به املاک":

        await update.message.reply_text(
        "🏡 بخش املاک",
        reply_markup=real_estate_menu()
        )

    elif text == "📈 بورس ایران":

        await update.message.reply_text(
            "بخش بورس ایران"
        )

    elif text == "🥇 صندوق‌های طلا":

        await update.message.reply_text(
            "بخش صندوق‌های طلا"
        )

    elif text == "🌍 فارکس":

        await update.message.reply_text(
            "بخش فارکس"
        )

    elif text == "🤖 چت با هوش مصنوعی":

        await update.message.reply_text(
            "هوش مصنوعی به زودی متصل می‌شود."
        )

    elif text == "⚙️ تنظیمات":

        await update.message.reply_text(
            "تنظیمات"
        )
