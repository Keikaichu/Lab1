#ex 1
#Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case.

class getString:
    def __init__(self):
        self.input_string = ""
    def getString(self):
        self.input_string = input()
    def printString(self):
        print(self.input_string.upper())
x = getString()
x.getString()
x.printString()

#ex 2
#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass
    def area(self):
        print('area of the shape:', 0)
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print("area of the square:", self.length ** 2)

shape = Shape()
shape.area()
square = Square(int(input()))
square.area()

#ex 3
#Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area of the shape:", 0)
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        
    def area(self):
        print("are of the rectangle:", self.length * self.width)
        
length = float(input())
width = float(input())
rectangle = Rectangle(length, width)
rectangle.area

#ex 4
"""Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points"""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance
x1=int(input())
y1=int(input())
point1=Point(x1,y1)
x2=int(input())
y2=int(input())
point2 = Point(x2,y2)
point1.show()
point2.show()
distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)  


#ex 5
#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
#class Account:     pass
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance: {self.balance}")
        else:
            print("Insufficient funds!")
owner = input("Enter the owner's name: ")
initial_balance = float(input("Enter the initial balance: "))
account = BankAccount(owner, initial_balance)
while True:
    print("\nChoose an action:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

#ex 6
#Write a program which can filter prime numbers in a list by using filter function. Note: Use lambda to define anonymous functions.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
nums = list(map(int,input().split()))
prime_nums = list(filter(lambda x: is_prime(x), nums))
print("primes in list:", prime_nums)