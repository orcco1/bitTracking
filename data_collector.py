import os
import pandas as pd
from binance.client import Client

def collect_historical_data(client, symbol, interval, days):
    try:
        print(f"⏳ Collecting data of {symbol}... Please wait")

        os.makedirs("data", exist_ok=True)

        # Obtain klines
        klines = client.get_historical_klines(symbol, interval, f"{days} days ago UTC")

        # Create DataFrame
        df = pd.DataFrame(klines, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "num_trades",
            "taker_buy_base_vol", "taker_buy_quote_vol", "ignore"
        ])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
        df.set_index("timestamp", inplace=True)

        # Save CSV
        path = f"data/{symbol}_{interval}_{days}d.csv".replace(":", "")
        df.to_csv(path)
        print(f"✅ Saved data in: {path}")
        
    except Exception as e:
        print(f"❌ Error al recolectar datos: {e}")
