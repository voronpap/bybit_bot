
import logging
from telegram import Update, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext

# Встановлення логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Команди Telegram-бота
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привіт! Я Telegram-бот для управління вашим торговим ботом.')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Список команд: \start, \help, \status, \trade_start, \trade_stop')

def status(update: Update, context: CallbackContext):
    update.message.reply_text('Статус: У процесі розробки.')

# Основна функція для запуску бота
def main():
    # Вставте свій токен Telegram API
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Реєстрація команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("status", status))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

from prediction import load_model, predict_strategy

# Завантаження моделі (вкажіть точний шлях до моделі)
MODEL_FILENAME = "model.pkl"
try:
    model = load_model(MODEL_FILENAME)
except FileNotFoundError:
    model = None
    print(f"Попередження: модель не знайдена за шляхом {MODEL_FILENAME}.")

# Команда для прогнозування стратегії
def suggest_strategy(update: Update, context: CallbackContext):
    if model is None:
        update.message.reply_text("Модель не завантажена. Будь ласка, навчіть модель перед використанням.")
        return

    # Очікується введення даних у форматі: "feature1,feature2,..."
    user_input = update.message.text.replace("/suggest_strategy ", "").strip()
    try:
        features = [float(x) for x in user_input.split(",")]
        strategy = predict_strategy(model, features)
        update.message.reply_text(f"Рекомендована стратегія: {strategy}")
    except ValueError:
        update.message.reply_text("Помилка: введіть правильні числові дані у форматі 'feature1,feature2,...'.")

# Додавання команди в основну функцію
def main():
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Реєстрація команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("suggest_strategy", suggest_strategy))

    # Запуск бота
    updater.start_polling()
    updater.idle()
