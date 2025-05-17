from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_config import BOT_TOKEN, CHAT_ID
from handlers import get_odds

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bem-vindo! Use /odds para ver as odds mais recentes.")

async def odds(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Buscando odds...")
    odds_msg = get_odds()
    await update.message.reply_text(odds_msg)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("odds", odds))

    app.bot.set_my_commands([
        BotCommand("start", "Iniciar o bot"),
        BotCommand("odds", "Ver odds mais recentes")
    ])

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()