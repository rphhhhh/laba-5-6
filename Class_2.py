class Car:
#Модель автомобиля для сервиса каршеринга
    def __init__(self, model):
#Инициализация состояния объекта
        self.model = model                       # модель
        self.fuel_level = 0                      # топливо 0–100
        self.is_engine_on = False                # двигатель выкл

    def start_engine(self):
#Заводит двигатель, если есть топливо
        if self.fuel_level <= 0:
            print("Нет топлива, завод невозможен")
            return
        self.is_engine_on = True
        print(f"{self.model}: двигатель заведён")

    def drive(self, km):
#Едет км (1 км = 1% топлива)
        if not self.is_engine_on:
            print("Сначала заведите двигатель!")
            return
        if km > self.fuel_level:
            print(f"Не хватает топлива на {km} км")
            return
        self.fuel_level -= km
        print(f"{self.model}: проехал {km} км, топливо {self.fuel_level}%")

    def refuel(self, liters):
#Заправка, лимит 100%
        self.fuel_level = min(100, self.fuel_level + liters)
        print(f"{self.model}: заправлено → {self.fuel_level}%")

    def stop_engine(self):
#Глушит двигатель
        self.is_engine_on = False
        print(f"{self.model}: двигатель заглушен")

if __name__ == "__main__":
    car1 = Car("Toyota Camry")
    car2 = Car("Kia Rio")

    print("--- car1 ---")
    car1.refuel(50)
    car1.start_engine()
    car1.drive(20)
    car1.stop_engine()

    print("\n--- car2 (изоляция) ---")
    car2.refuel(30)
    car2.start_engine()
    car2.drive(10)
    print(f"car1: {car1.fuel_level}%, car2: {car2.fuel_level}%")  # независимы