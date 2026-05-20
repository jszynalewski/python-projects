from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import requests
import os
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

TOKEN = os.getenv("TOKEN")

EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")


async def start(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Cześć jestem botem, niżej masz komendy:
/start - wyswietla wiadomość startową
/pogoda [miasto] - wyswietla pogode
/waluta [waluta] - sprawdza kurs walut do PLN
/wymiana [kwota] [waluta z] [waluta do] - przelicznik walut
/krypto [kryptowaluta] - pokazuje wartość bitcoina i ethereum
""")

async def pogoda(update : Update, context : ContextTypes.DEFAULT_TYPE):
    if context.args:
        city = context.args[0]
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=pl"
        response = requests.get(url)
        data = response.json()
        temp = data["main"]["temp"]
        temp = round(temp)
        miasto = data["name"]
        description = data["weather"][0]["description"]
        await update.message.reply_text(f"{miasto} temperatura wynosi {temp} stopni Celcjusza i jest {description}")
    else:
        await update.message.reply_text("Nie podano miasta")

async def waluta(update : Update, context : ContextTypes.DEFAULT_TYPE):
    if context.args:
        kwota = 1
        walutaZ = context.args[0]
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{walutaZ}/PLN/{kwota}"
        response = requests.get(url)
        data = response.json()
        wynik = data["conversion_result"]
        wynik = round(wynik, 2)
        await update.message.reply_text(f"{kwota}{walutaZ} = {wynik}PLN")
    else:
        await update.message.reply_text("Nie podano waluty")

async def krypto(update : Update, context : ContextTypes.DEFAULT_TYPE):
    if context.args:
        kryptowaluta = context.args[0]
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={kryptowaluta}&vs_currencies=usd,pln"
        response = requests.get(url)
        data = response.json()
        wynik = data[kryptowaluta]["pln"]
        await update.message.reply_text(f"{kryptowaluta} = {wynik}PLN")
    else:
        await update.message.reply_text("Nie podano kryptowaluty")


async def wymiana(update : Update, context : ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 3:
        kwota = context.args[0]
        walutaZ = context.args[1]
        walutaDo = context.args[2]
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{walutaZ}/{walutaDo}/{kwota}"
        response = requests.get(url)
        data = response.json()
        wynik = data["conversion_result"]
        await update.message.reply_text(f"{kwota}{walutaZ} = {wynik}{walutaDo}")
    else:
        await update.message.reply_text("Nie podano wszystkich danych")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pogoda", pogoda))
app.add_handler(CommandHandler("waluta", waluta))
app.add_handler(CommandHandler("krypto", krypto))
app.add_handler(CommandHandler("wymiana", wymiana))
app.run_polling()

