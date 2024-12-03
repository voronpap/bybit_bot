
from flask import Flask
from web.routes import initialize_routes
from monitoring.logging import setup_logging
from monitoring.notifications import start_telegram_bot
from threading import Thread
from config.settings import TELEGRAM_BOT_TOKEN

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Ініціалізація логування
setup_logging()

# Ініціалізація маршрутів Flask
initialize_routes(app)

# Функція для запуску Telegram-бота у фоновому потоці
def run_telegram_bot():
    start_telegram_bot(TELEGRAM_BOT_TOKEN)

# Головний запуск
if __name__ == "__main__":
    # Запуск Telegram-бота в окремому потоці
    telegram_thread = Thread(target=run_telegram_bot)
    telegram_thread.start()

    # Запуск Flask-додатка
    app.run(host="0.0.0.0", port=5000)
