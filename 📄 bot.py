import os
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load token from Railway-provided env variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# WebApp URLs
BASE_URL = "https://www.alphabetcouncil.com"
URLS = {
    "start": BASE_URL,
    "trade": f"{BASE_URL}/dashboard",
    "wallet": f"{BASE_URL}/wallet",
    "airdrop": f"{BASE_URL}/airdrop"
}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🚀 Launch TraderGPT", web_app=WebAppInfo(url=URLS["start"]))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to TraderGPT by BlockSmithAI! Tap below to begin:", reply_markup=reply_markup)

# /trade command
async def trade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🧠 Launch Trading Terminal", web_app=WebAppInfo(url=URLS["trade"]))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Launching trading terminal...", reply_markup=reply_markup)

# /wallet command
async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔐 Open Wallet Generator", web_app=WebAppInfo(url=URLS["wallet"]))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Access your quantum-secure wallet setup:", reply_markup=reply_markup)

# /airdrop command
async def airdrop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ref_link = f"{URLS['airdrop']}?ref={update.effective_user.id}"
    keyboard = [[InlineKeyboardButton("💸 Join Airdrop", web_app=WebAppInfo(url=ref_link))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Participate in our gamified airdrop & earn XP!", reply_markup=reply_markup)

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
Available Commands:
/start - Launch the TraderGPT App
/trade - Open the AI trading terminal
/wallet - Generate your wallet
/airdrop - Join the airdrop campaign
/help - Show help menu
""")

# Application
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("trade", trade))
app.add_handler(CommandHandler("wallet", wallet))
app.add_handler(CommandHandler("airdrop", airdrop))
app.add_handler(CommandHandler("help", help_command))

if __name__ == '__main__':
    app.run_polling()
