class EWallet:
#Кошелёк с контролем баланса и дневного лимита
    def __init__(self, user_id, balance=0, daily_limit=10000):
        self.user_id = user_id                   # публичный атрибут
        self.balance = balance                   # через сеттер (валидация)
        self.daily_limit = daily_limit           # через сеттер (валидация)

#жёсткая валидация
    @property
    def balance(self):
#Геттер: текущий баланс
        return self.__balance

    @balance.setter
    def balance(self, value):
#Сеттер: баланс не может быть < 0 → ValueError
        if value < 0:
            raise ValueError("Баланс не может быть ниже нуля!")
        self.__balance = value

#мягкая валидация
    @property
    def daily_limit(self):
        """Геттер: дневной лимит."""
        return self.__daily_limit

    @daily_limit.setter
    def daily_limit(self, value):
#Сеттер: лимит < 0 → ставим 0 + предупреждение
        if value < 0:
            print("Предупреждение: лимит < 0 → установлен 0")
            value = 0
        self.__daily_limit = value

    def deposit(self, amount):
#Пополнение через сеттер
        self.balance += amount
        print(f"+{amount} → баланс {self.balance}")

    def withdraw(self, amount):
#Списание с проверкой через геттер
        if amount > self.balance:
            raise ValueError(f"Недостаточно: есть {self.balance}, нужно {amount}")
        self.balance -= amount
        print(f"-{amount} → баланс {self.balance}")

if __name__ == "__main__":
    print("=== 1. Успешное создание ===")
    w1 = EWallet("user_001", 5000, 3000)
    print(f"id={w1.user_id}, balance={w1.balance}, limit={w1.daily_limit}")
    w1.deposit(1000)
    w1.withdraw(500)

    print("\n=== 2. Нарушение инвариантов ===")
    w1.daily_limit = -100                        # мягкая → 0
    print(f"limit: {w1.daily_limit}")
    try:
        w1.withdraw(10000)                       # жёсткая → ValueError
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n=== 3. Приватность / Name Mangling ===")
    try:
        print(w1.__balance)                      # AttributeError
    except AttributeError:
        print("Прямой доступ к __balance запрещён")
    print(f"Через _EWallet__balance: {w1._EWallet__balance}")  # обход (для демо)

    print("\n=== 4. Изоляция ===")
    w2 = EWallet("user_002", 100)
    w2.balance = 0
    print(f"w1={w1.balance}, w2={w2.balance} — независимы")