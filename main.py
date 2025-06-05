import json
import time
from binance.client import Client
import checkerTracker

with open("config.json") as f:
    config = json.load(f)

client = Client(config["api_key"], config["api_secret"])

# Create Main Menu With Options

print("--Welcome to BITTRACKING--")
print("1. Track specific symbol price")
print("2. Check specific symbol price")
print("3. Check available symbols")
menu_option = input("Please select an option: ")


if menu_option == "1":
    symbol = input("Enter symbol to track (e.g. BTCUSDT): ").upper()
    threshold = float(input("Alert if price drops below: "))
    checkerTracker.tracker(client, symbol, threshold)

elif menu_option == "2":
    symbol = input("Enter symbol to check price (e.g. ETHUSDT): ").upper()
    price = client.get_symbol_ticker(symbol=symbol)
    checkerTracker.checker(client, symbol)

elif menu_option == "3":
    available_symbols = checkerTracker.available_symbols(client)
    print(f"Available symbols: {len(available_symbols)}")
    print(", ".join(available_symbols[:50]))

else:
    print("Invalid option. Exiting.")
