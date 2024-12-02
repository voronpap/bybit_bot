from config import API_KEY, API_SECRET, SYMBOL, POSITION_SIZE, PROFIT_PERCENT
from data_handler import fetch_market_data
from prediction import load_model, make_prediction
from trade import open_position
import bybit

# Підключення до Bybit
def get_client(api_key, api_secret):
    return bybit.bybit(test=False, api_key=api_key, api_secret=api_secret)

# Основний цикл бота
def bot_loop(client, symbol, position_size, profit_percent):
    model = load_model()
    print(f"Бот запущено для {symbol}!")
    
    while True:
        market_data = fetch_market_data(client, symbol)
        if market_data is not None:
            prediction = make_prediction(model, market_data)
            print(f"Передбачення: {prediction}")
            
            # Торгове рішення
            if prediction == 1:  # Припустимо, 1 — ріст
                open_position(client, symbol, side="Buy", size=position_size)
            elif prediction == -1:  # -1 — падіння
                open_position(client, symbol, side="Sell", size=position_size)
        else:
            print("Дані недоступні, повтор через 60 секунд.")
        
        time.sleep(60)

if __name__ == "__main__":
    client = get_client(API_KEY, API_SECRET)
    bot_loop(client, SYMBOL, POSITION_SIZE, PROFIT_PERCENT)
