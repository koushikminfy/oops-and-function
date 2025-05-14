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

