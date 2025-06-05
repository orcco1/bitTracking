import json
import time
from binance.client import Client
import checkerTracker
import data_collector

with open("config.json") as f:
    config = json.load(f)

client = Client(config["api_key"], config["api_secret"])

# Create Main Menu With Options

print("--Welcome to BITTRACKING--")
print("1. Track specific symbol price")
print("2. Check specific symbol price")
print("3. Check available symbols")
print("4. Obtain symbol relevant data")
menu_option = input("Please select an option: ")


if menu_option == "1":
    symbol = input("Enter symbol to track (e.g. BTCUSDT): ").upper()
    threshold = float(input("Alert if price drops below: "))
    checkerTracker.tracker(client, symbol, threshold)

elif menu_option == "2":
    symbol = input("Enter symbol to check price (e.g. ETHUSDT): ").upper()
    checkerTracker.checker(client, symbol)

elif menu_option == "3":
    available_symbols = checkerTracker.available_symbols(client)
    print(f"Available symbols: {len(available_symbols)}")
    print(", ".join(available_symbols[:50]))

elif menu_option == "4":
    symbol = input("Enter symbol (e.g. BTCUSDT): ").upper()
    days = int(input("Enter number of days to collect (e.g. 30): "))
    interval = input("Enter interval (e.g. 1h, 15m): ").lower()

    interval_map = {
        "1m": Client.KLINE_INTERVAL_1MINUTE,
        "3m": Client.KLINE_INTERVAL_3MINUTE,
        "5m": Client.KLINE_INTERVAL_5MINUTE,
        "15m": Client.KLINE_INTERVAL_15MINUTE,
        "30m": Client.KLINE_INTERVAL_30MINUTE,
        "1h": Client.KLINE_INTERVAL_1HOUR,
        "4h": Client.KLINE_INTERVAL_4HOUR,
        "1d": Client.KLINE_INTERVAL_1DAY
    }

    if interval not in interval_map:
        print("Invalid interval.")
    else:
        data_collector.collect_historical_data(client, symbol, interval_map[interval], days)

else:
    print("Invalid option. Exiting.")
