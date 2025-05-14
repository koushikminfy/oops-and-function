#MEdium
#1.question I


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors, fuel_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.fuel_type = fuel_type

    def display_car_info(self):
        self.display_info()
        print(f"Doors: {self.doors}")
        print(f"Fuel Type: {self.fuel_type}")

car = Car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(car.make)
print(car.doors)
car.display_car_info()


#2. Queestion II


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


account = BankAccount("123456", 1000)
print(account.get_balance())
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())
print(account.get_account_number())

try:
    account.__balance = 2000
except AttributeError:
    print("Cannot directly access private attribute")
