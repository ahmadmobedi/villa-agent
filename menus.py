from telegram import ReplyKeyboardMarkup


def main_menu():
    keyboard = [
        ["🏡 املاک", "📈 بورس ایران"],
        ["🥇 صندوق‌های طلا", "🌍 فارکس"],
        ["🤖 چت با هوش مصنوعی", "⚙️ تنظیمات"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

def real_estate_menu():
    keyboard = [
        ["🏠 ثبت ملک", "🔍 جستجوی ملک"],
        ["📋 فایل‌های من", "❤️ علاقه‌مندی‌ها"],
        ["📊 تحلیل بازار"],
        ["🔙 بازگشت"]
    ]

def market_analysis_menu():
    keyboard = [
        ["📈 روند قیمت", "🏘 مقایسه مناطق"],
        ["💰 قیمت هر متر", "📊 گزارش روز بازار"],
        ["📍 نقشه قیمت‌ها"],
        ["🔙 بازگشت به املاک"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
