from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")  # Ovo ćeš postaviti na Renderu kao SECRET

# JEZICI
languages = ["ENGLISH", "ITALIANO"]

# PROMOCIJE
promotions = {
english_promos = [
    {
        "image": "https://betbytebusiness.com/wp-content/uploads/2025/03/tg-mro-picture.jpg",
        "text": """🎁🎁🎁 UP TO $210 TOTAL

Here’s what you need to do: ⭐️ Sign up at MROCASINO 
⭐️ Enter the promo code TGCHIP (after registration) 

Terms:

🗒: Value:$210 Free Chip 7 days per $30: The Arcane Unlocked; Wagering: x30; Max cash out: $30; Max bet per hand: $10; Allowed games: NP Slots Only; Allowed countries: US, Canada, New Zealand, Italy, Germany, Sweden, Norway

Benefits of MRO CASINO: 
🔥 Welcome package 400% + 400 FS 
🔥 High RTP 
🔥 VIP Program
🔥 A lot of Bonuses

Click the button "TAKE BONUS" below to register and claim your bonus 👇""",
        "button": "🎰 TAKE BONUS",
        "url": "https://mrocasino.com"
    },
    {
        "image": "https://betbytebusiness.com/wp-content/uploads/2025/03/tg-eternal-picture.jpg",
        "text": """🎁🎁🎁 FREE SPIN FOREVER

Here’s what you need to do: ⭐️ Sign up at ETERNALSLOTS 
⭐️ Enter the promo code TGFREE (after registration) 

Terms:

🗒: 224 spins on Cash Bandits 3; 1st Bonus + free spins every day forever (30 per day). Code: 224SPINS; Wagering: x30; Max cash out: $100; Max bet per hand: None; Allowed games: Non-progressive slots, Keno, Video Poker, Blackjack; Allowed countries: US, Canada, Australia, New Zealand, Italy, Germany, Sweden, Norway; Note: Free spins stop being available if more than 10 free promotions have been claimed without a deposit in-between. Only one withdrawal from free promotion is allowed between deposits.

Benefits of ETERNAL SLOTS: 
🔥 Welcome package 1000% + 1000 FS 
🔥 High RTP 
🔥 VIP Program
🔥 FREE SPINS FOREVER

Click the button "TAKE BONUS" below to register and claim your bonus 👇""",
        "button": "🎰 TAKE BONUS",
        "url": "https://eternalslots.com"
    },
    {
        "image": "https://betbytebusiness.com/wp-content/uploads/2025/03/tg-goat-picture.jpg",
        "text": """🎁🎁🎁 75 FREE CHIP

Here’s what you need to do: ⭐️ Sign up at GOATSPINS 
⭐️ Enter the promo code TG-CHIP (after registration) 

Terms:

🗒: Value: $75 Free Chip; Wagering: x30; Max cash out: $30; Max bet per hand: $10; Allowed games: Non-progressive slots; Allowed countries: US, Canada, New Zealand, Italy, Germany, Sweden, Norway (but WE ARE VPN FRIENDLY, use USA VPN).

Benefits of Goat Spins: 
🔥 Welcome package 1000% + 1000 FS 
🔥 Vpn Friendly 
🔥 NO KYC
🔥 No Max Cashout Bonuses

Click the button "TAKE BONUS" below to register and claim your bonus 👇""",
        "button": "🎰 TAKE BONUS",
        "url": "https://goatspins.com"
    }
]

german_promos = [
    {
        "image": "https://betbytebusiness.com/wp-content/uploads/2025/03/tg-mro-picture.jpg",
        "text": """🎁🎁🎁 BIS ZU 210 $ GESAMT

So funktioniert’s:⭐️ Registriere dich bei MROCASINO
⭐️ Gib nach der Registrierung den Promo-Code TGCHIP ein

Bedingungen:
🗒: Wert: 210 $ Free Chip – 7 Tage lang je 30 $: The Arcane Unlocked
Umsatzbedingungen: x30
Maximale Auszahlung: 30 $
Maximaler Einsatz pro Runde: 10 $
Erlaubte Spiele: Nur NP Slots
Erlaubte Länder: USA, Kanada, Neuseeland, Italien, Deutschland, Schweden, Norwegen

Vorteile von MRO CASINO:
🔥 Willkommenspaket: 400 % + 400 Freispiele
🔥 Hohe RTP
🔥 VIP-Programm
🔥 Viele Boni

Klicke auf den Button „BONUS HOLEN“ unten, um dich zu registrieren und deinen Bonus zu sichern 👇""",
        "button": "🎰 BONUS HOLEN",
        "url": "https://mrocasino.com"
    },
    {
        "image": "https://betbytebusiness.com/wp-content/uploads/2025/03/tg-eternal-picture.jpg",
        "text": """🎁🎁🎁 KOSTENLOSE FREISPIELE FÜR IMMER

So funktioniert’s:⭐️ Registriere dich bei ETERNALSLOTS
⭐️ Gib nach der Registrierung den Promo-Code TGFREE ein

Bedingungen:
🗒: 224 Freispiele auf Cash Bandits 3

Bonus + jeden Tag für immer Freispiele (30 pro Tag)
Code: 224SPINS
Umsatzbedingungen: x30
Maximale Auszahlung: 100 $
Maximaler Einsatz pro Runde: Kein Limit
Erlaubte Spiele: Nicht-progressive Slots, Keno, Video Poker, Blackjack
Erlaubte Länder: USA, Kanada, Australien, Neuseeland, Italien, Deutschland, Schweden, Norwegen
⚠️ Hinweis: Freispiele sind nicht mehr verfügbar, wenn mehr als 10 Gratisaktionen ohne Einzahlung dazwischen beansprucht wurden.
Nur eine Auszahlung aus Gratisaktionen ist zwischen Einzahlungen erlaubt.

Vorteile von ETERNAL SLOTS:
🔥 Willkommenspaket: 1000 % + 1000 Freispiele
🔥 Hohe RTP
🔥 VIP-Programm
🔥 FREISPIELE FÜR IMMER

Klicke auf den Button „BONUS HOLEN“ unten, um dich zu registrieren und deinen Bonus zu sichern 👇""",
        "button": "🎰 BONUS HOLEN",
        "url": "https://eternalslots.com"
    },
    {
        "image": "https://betbytebusiness.com/wp-content/uploads/2025/03/tg-goat-picture.jpg",
        "text": """🎁🎁🎁 75 $ FREE CHIP

So funktioniert’s:⭐️ Registriere dich bei GOATSPINS
⭐️ Gib nach der Registrierung den Promo-Code TG-CHIP ein

Bedingungen:
🗒: Wert: 75 $ Free Chip
Umsatzbedingungen: x30
Maximale Auszahlung: 30 $
Maximaler Einsatz pro Runde: 10 $
Erlaubte Spiele: Nicht-progressive Slots
Erlaubte Länder: USA, Kanada, Neuseeland, Italien, Deutschland, Schweden, Norwegen
🌍 Aber wir sind VPN-freundlich – nutze ein VPN mit Standort USA!

Vorteile von GOAT SPINS:
🔥 Willkommenspaket: 1000 % + 1000 Freispiele
🔥 VPN-freundlich
🔥 Kein KYC
🔥 Keine Max-Cashout-Boni

Klicke auf den Button „BONUS HOLEN“ unten, um dich zu registrieren und deinen Bonus zu sichern 👇""",
        "button": "🎰 BONUS HOLEN",
        "url": "https://goatspins.com"
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
