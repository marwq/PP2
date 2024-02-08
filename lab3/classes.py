from __future__ import annotations

# 1. Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class Class1:
    def __init__(self):
        self.string = ""
    
    def get_string(self):
        self.string = input("Enter a string: ")
    
    def print_string(self):
        print(self.string.upper())
        
        
# 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        self._area = 0
    
    def area(self):
        print(self._area)
    
class Square(Shape):
    def __init__(self, length: int):
        self.length = length
        self._area = length ** 2
        

# 3. Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        
    def compute_area(self):
        self._area = self.length * self.width
        

# 4. Write the definition of a Point class.

'''
Objects from this class should have a
 - a method show to display the coordinates of the point
 - a method move to change these coordinates
 - a method dist that computes the distance between 2 points
'''

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, x: int, y: int):
        self.x += x
        self.y += y
    
    def dist(self, other: Point) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    

# 5. Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            

# 6. Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.

from .functions_1 import is_prime

def filter_prime(numbers: list[int]) -> list[int]:
    prime_numbers = list(filter(is_prime, numbers))
    return prime_numbers