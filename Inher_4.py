class SmartDevice:
#Базовый класс умного устройства
    def __init__(self, name, power):
        self.name, self.power, self.is_on = name, power, False  # общие атрибуты
    def turn_on(self):
        self.is_on = True; print(f"{self.name} вкл → {self.power} Вт")   # наследуется
    def turn_off(self):
        self.is_on = False; print(f"{self.name} выкл → 0 Вт")            # наследуется
    def do_work(self):
        print(f"{self.name}: работает")                                  # будет переопределён
    def get_info(self):
        return f"{self.name} | {self.power} Вт | {'Вкл' if self.is_on else 'Выкл'}"

class Refrigerator(SmartDevice):
#Холодильник
    def __init__(self, name, power, capacity):
        super().__init__(name, power)                                    # super() обязателен
        self.temp, self.capacity = 4, capacity
    def do_work(self):
        print(f"[{self.name}] Охлаждает до {self.temp}°C ({self.capacity} л)")
    def get_info(self):
        return f"Холодильник {self.name} | {self.power} Вт | {self.temp}°C | {self.capacity} л"
    def set_temperature(self, t):                                        # уникальный метод
        self.temp = t; print(f"{self.name}: температура {t}°C")


class WashingMachine(SmartDevice):
#Стиральная машина
    def __init__(self, name, power):
        super().__init__(name, power)
        self.program, self.load = "Хлопок", 0
    def do_work(self):
        print(f"[{self.name}] Стирает: {self.program} ({self.load} кг)")
    def get_info(self):
        return f"Стиралка {self.name} | {self.power} Вт | {self.program} | {self.load} кг"
    def select_program(self, p):                                         # уникальный метод
        self.program = p; print(f"{self.name}: программа {p}")

class AirConditioner(SmartDevice):
#Кондиционер
    def __init__(self, name, power):
        super().__init__(name, power)
        self.target, self.mode = 22, "охлаждение"
    def do_work(self):
        print(f"[{self.name}] {self.mode} до {self.target}°C")
    def get_info(self):
        return f"Кондиционер {self.name} | {self.power} Вт | {self.target}°C | {self.mode}"
    def change_mode(self, m):                                            # уникальный метод
        self.mode = m; print(f"{self.name}: режим {m}")

if __name__ == "__main__":
    print("=== ДЕМО: УМНАЯ ТЕХНИКА ===")
    fridge = Refrigerator("Samsung", 150, 350)
    washer = WashingMachine("LG", 2000)
    ac = AirConditioner("Daikin", 1000)

    print("\n[1] Создание:", fridge.name, washer.name, ac.name)

    print("\n[2] Унаследованные методы")
    fridge.turn_on(); washer.turn_on(); ac.turn_on()

    print("\n[3] Переопределённые do_work / get_info")
    fridge.do_work(); print(fridge.get_info())
    washer.load = 5; washer.do_work(); print(washer.get_info())
    ac.do_work(); print(ac.get_info())

    print("\n[4] Уникальные методы")
    fridge.set_temperature(2)
    washer.select_program("Шерсть")
    ac.change_mode("обогрев")

    print("\n[5] Изоляция состояний")
    fridge.turn_off()
    print(f"Samsung выкл, LG={washer.is_on}, Daikin={ac.is_on}")