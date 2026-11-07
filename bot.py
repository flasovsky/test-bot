from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "9141857050:AAHBJszACNp74Je5O-Ip7EWBuUaOW0fDSSI"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я простой бот.\n"
        "Напиши что-нибудь, и я повторю это.\n"
        "Команды: /start, /help"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я умею:\n"
        "• /start — начать\n"
        "• /help — показать справку\n"
        "• Повторять текстовые сообщения"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)


def main():
    if not TOKEN:
        raise ValueError("Установи переменную окружения BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
