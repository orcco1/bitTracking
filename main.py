import json
import time
from binance.client import Client

with open("config.json") as f:
    config = json.load(f)

client = Client(config["api_key"], config["api_secret"])

# Tracking
symbol = "BTCUSDT"
alert_threshold = 60000.0

print(f"Tracking {symbol}... Alert if dips under ${alert_threshold}")

while True:
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        price = float(ticker['price'])
        print(f"[{time.strftime('%H:%M:%S')}] Actual prince: ${price:.2f}")

        if price < alert_threshold:
            print(f"🚨 Alert: {symbol} dips under ${alert_threshold} → actual price: ${price:.2f}")

        time.sleep(30)
    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(10)
