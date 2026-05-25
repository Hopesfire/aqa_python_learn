class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        return f"Марка: {self.brand}, модель: {self.model}, год выпуска: {self.year}"


car1 = Car("Mercedes", "C-Class", 2020)
car2 = Car("BMW", "X5", 1999)
car3 = Car("Audi", "A4", 2000)

print(car1.print_car_info())
print(car2.print_car_info())
print(car3.print_car_info())
