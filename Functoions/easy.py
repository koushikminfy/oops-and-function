# EASY FUNCTIONS

# 1. Function Basics
def calculate_avg(numbers):
    total = 0
    if not numbers:
        return 0
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

print(calculate_avg([5, 10, 15, 20]))    
print(calculate_avg([]))                 


# 2. Default Parameters
def greet_user(name, greet="Hello"):
    return f"{greet},{name}!"

print(greet_user("Alice"))              
print(greet_user("Bob", "Hi"))          



# MEDIUM FUNCTIONS

# 1. Variable Arguments
def calculate_total(*prices, discount=0):
    total = sum(prices)
    if discount:
        amount = total * (discount / 100)
        total = total - amount
        return f"{total}({discount}% off)"
    return total

print(calculate_total(10, 20, 30))                    
print(calculate_total(10, 20, 30, discount=10))        


# 2. Closures
def create_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))   
print(triple(5))   




class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
        
    def perimeter(self):
        return 2*(self.width+self.height)



# Example usage
rect = Rectangle(5, 10)
print(rect.area())  # Should return 50
print(rect.perimeter())  # Should return 30


class Counter:
    def __init__(self,value=0):
        self.value=value
    def increment(self):
        self.value +=1
        return self.value 
    def decrement(self):
        self.value -=1
        return self.value 
    def reset(self):
        self.value =0
        return self.value

counter = Counter()
counter.increment()
counter.increment()
print(counter.value)
counter.decrement()
print(counter.value)  
counter.reset()
print(counter.value)  





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
