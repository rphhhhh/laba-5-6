class ShopError(Exception):
#Базовое исключение магазина
    pass
class OutOfStockError(ShopError):
#Товар закончился
    def __init__(self, item_name, requested_qty, available_qty):
        self.item_name = item_name               # контекст: название
        self.requested_qty = requested_qty       # сколько хотели
        self.available_qty = available_qty       # сколько есть
        super().__init__(f"'{item_name}': нужно {requested_qty}, есть {available_qty}")

class InvalidPromoCodeError(ShopError):
#Промокод недействителен
    def __init__(self, promo_code):
        self.promo_code = promo_code             # контекст: сам код
        super().__init__(f"Промокод '{promo_code}' недействителен")

def process_order(item_name, qty, available_qty, promo_code):
#Валидатор: проверяет склад и промокод, иначе raise
    if qty > available_qty:                      # проверка остатка
        raise OutOfStockError(item_name, qty, available_qty)
    if promo_code and promo_code not in {"SALE10", "WELCOME", "NEWYEAR"}:
        raise InvalidPromoCodeError(promo_code)  # неизвестный промо
    return f"Заказ: {item_name} x{qty}, промо: {promo_code or 'нет'}"

if __name__ == "__main__":
    # 1. Успех
    try:
        print(process_order("Ноутбук", 1, 5, "SALE10"))
    except ShopError as e:
        print("Ошибка:", e)
    # 2. Не хватает товара
    try:
        print(process_order("Мышь", 5, 2, None))
    except OutOfStockError as e:
        print(f"Склад: {e.item_name} — нужно {e.requested_qty}, есть {e.available_qty}")
    # 3. Плохой промокод
    try:
        print(process_order("Клавиатура", 1, 10, "SALE2026"))
    except InvalidPromoCodeError as e:
        print(f"Промокод отклонён: {e.promo_code}")