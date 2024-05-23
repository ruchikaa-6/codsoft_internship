#Simple calculator
def options():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exponential")
    print("6.power")
    print("7.squareroot")
    print("8.Exit")
def addition(a,b):
    r=a+b
    return r
def subtraction(a,b):
    r=a-b
    return r
def multiplication(a,b):
    r=a*b
    return r
def division(a,b):
    if(b==0):
        print("Can't divided by zero")
    else:
        r=a/b
        return r
import math
def exponential(a):
    return math.exp(a)
def power(a,b):
    return math.pow(a,b)
def sqrt(a):
    return math.sqrt(a)
options()
while True:
    option=int(input("Enter your choice:"))
    if option == 1:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        print(addition(a,b))
    elif option == 2:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        print(subtraction(a,b))
    elif option == 3:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        print(multiplication(a,b))
    elif option == 4:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        print(division(a,b))
    elif option == 5:
        a = int(input("Enter the number:"))
        print(exponential(a))
    elif option == 6:
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number:"))
        print(power(a,b))
    elif option == 7:
        a=int(input("Enter the number:"))
        print(sqrt(a))
    elif option == 8:
        break
    else:
        print("Invalid choice. Please try again.")