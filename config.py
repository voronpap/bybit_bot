from dotenv import load_dotenv
import os

# Завантаження .env
load_dotenv()

# API ключі
API_KEY = os.getenv("BYBIT_API_KEY")
API_SECRET = os.getenv("BYBIT_API_SECRET")

# Основні параметри
SYMBOL = "BTCUSDT"
POSITION_SIZE = 0.01
PROFIT_PERCENT = 0.5
