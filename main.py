import json
from binance.client import Client

with open("config.json") as f:
    config = json.load(f)

client = Client(config["api_key"], config["api_secret"])

price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"Precio actual BTC/USDT: {price['price']}")
