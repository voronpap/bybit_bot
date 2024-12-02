def open_position(client, symbol, side, size):
    """Відкриття торгової позиції."""
    try:
        client.Order.Order_new(symbol=symbol, side=side, order_type="Market", qty=size).result()
        print(f"Позиція {side} відкрита для {symbol} розміром {size}.")
    except Exception as e:
        print(f"Помилка відкриття позиції: {e}")
