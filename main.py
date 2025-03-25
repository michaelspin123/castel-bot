from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")  # Ovo ćeš postaviti na Renderu kao SECRET

# JEZICI
languages = ["ENGLISH", "ITALIANO"]

# PROMOCIJE
promotions = {
    "ENGLISH": [
        {
            "title": "🎁 Claim 250 no-deposit free spins in Cash Bandits by RTG!",
            "desc": """Here’s what you need to do: 
⭐️ Sign up at MROCASINO 
⭐️ Enter the promo code GEM250 (after registration)

Where to enter the promo code?
⚡️ Mobile Version: Profile > Promo > Casino VIP Cashback > Bonuses
⚡️ PC Version: Profile > Bonuses & Gifts

Benefits of MROCASINO: 
🔥 Welcome package 1500 EUR + 150 FS 
🔥 High RTP 
🔥 Loyalty program 
🔥 A lot of Bonuses""",
            "button_text": "🎰 TAKE BONUS",
            "button_url": "https://mrocasino.com"
        },
        {
            "title": "😎 Sign up at Eternal Slots and claim an amazing welcome bonus - FREE SPINS FOREVER!",
            "desc": """⚡️ Welcome package of 1200 EUR + 220 free spins

Benefits of ETERNAL SLOTS Casino: 
🔥 Licensed casino
🔥 High RTP 
🔥 Excellent loyalty program 
🔥 Lotteries and tournaments 
🔥 Sportsbook

Click the button below to register and claim your bonus 👇""",
            "button_text": "🎰 TAKE BONUS",
            "button_url": "https://eternalslots.com"
        }
    ]
}

# START poruka
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("START", callback_data="choose_language")]]
    await update.message.reply_text(
        text="WHAT CAN THIS BOT DO?\n\n- Free Spins Forever\n- Personalized bonuses and updates",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# /menu komanda
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await choose_language(update, context)

# Izbor jezika
async def choose_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()
        send = query.edit_message_text
    else:
        send = update.message.reply_text

    keyboard = [[InlineKeyboardButton(lang, callback_data=f"lang_{lang}")] for lang in languages]
    await send(
        text="Please choose your language or country:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Prikaz prve promocije
async def language_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = query.data.replace("lang_", "")
    context.user_data["lang"] = lang
    context.user_data["promo_index"] = 0
    await show_promo(query, context)

# Prikaz sledeće promocije
async def next_promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = context.user_data.get("lang", "ENGLISH")
    context.user_data["promo_index"] += 1
    await show_promo(query, context)

# Prikaz promocije
async def show_promo(query, context):
    lang = context.user_data.get("lang", "ENGLISH")
    index = context.user_data.get("promo_index", 0)
    promo_list = promotions.get(lang, [])

    if index >= len(promo_list):
        context.user_data["promo_index"] = 0
        index = 0

    promo = promo_list[index]
    keyboard = [
        [InlineKeyboardButton(promo["button_text"], url=promo["button_url"])],
    ]

    # Ako ima još promocija, dodaj NEXT dugme
    if len(promo_list) > 1:
        keyboard.append([InlineKeyboardButton("➡️ NEXT CASINO", callback_data="next_promo")])

    keyboard.append([InlineKeyboardButton("🏠 MENU", callback_data="choose_language")])

    await query.edit_message_text(
        text=f"{promo['title']}\n\n{promo['desc']}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Main
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(CallbackQueryHandler(choose_language, pattern="^choose_language$"))
    app.add_handler(CallbackQueryHandler(language_selected, pattern="^lang_"))
    app.add_handler(CallbackQueryHandler(next_promo, pattern="^next_promo$"))

    app.run_polling()
