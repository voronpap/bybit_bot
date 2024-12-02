import pandas as pd

def fetch_market_data(client, symbol, interval="1m", limit=100):
    """Отримує історичні дані про ціни з Bybit."""
    try:
        response = client.Kline.Kline_get(symbol=symbol, interval=interval, limit=limit).result()[0]
        if response['ret_code'] == 0:
            data = response['result']
            df = pd.DataFrame(data)
            df['timestamp'] = pd.to_datetime(df['open_time'], unit='s')
            return df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
        else:
            print("Помилка отримання даних.")
            return None
    except Exception as e:
        print(f"Помилка отримання ринкових даних: {e}")
        return None
