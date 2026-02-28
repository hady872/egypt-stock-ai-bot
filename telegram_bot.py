from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pandas as pd
from analysis import analyze_stock

from config import TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Egypt Stock AI Bot 📈")


async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    df = pd.read_csv("data/SKPC.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    result = analyze_stock(df)

    await update.message.reply_text(result)


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analyze", analyze))

    app.run_polling()


if __name__ == "__main__":
    main()