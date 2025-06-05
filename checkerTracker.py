import time

def tracker(client, symbol, alert_threshold):
    while True:
        try:
            ticker = client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])
            print(f"[{time.strftime('%H:%M:%S')}] Actual price of {symbol}: ${price:.2f}")

            if price < alert_threshold:
                print(f"🚨 Alert: {symbol} dipped under ${alert_threshold} → current price: ${price:.2f}")

            time.sleep(30)
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(10)

def checker(client, symbol):
    try:
        price = float(client.get_symbol_ticker(symbol=symbol)['price'])
        print(f"💰 Current price of {symbol}: ${price:.2f}")
    except Exception as e:
        print(f"❌ Error checking price: {e}")

def available_symbols(client):
    try:
        exchange_info = client.get_exchange_info()
        symbols = [s['symbol'] for s in exchange_info['symbols']]
        return symbols
    except Exception as e:
        print(f"❌ Error obtaining symbols: {e}")
        return []
