import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام ✨سایه✨ عزیز! استودیوی هوش مصنوعی تو آماده‌ست.\nمتن شعرت رو بفرست تا برات تبدیل به موزیک کنم!")

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, f"درخواستت دریافت شد:\n«{message.text}»\nدر حال پردازش قطعه صوتی...")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
