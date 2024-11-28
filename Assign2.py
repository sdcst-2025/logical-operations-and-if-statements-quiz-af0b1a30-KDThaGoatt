"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

x = float(input("Enter a number"))
y = float(input("Enter another number"))
answer = (input("Is one of the numbers the hypotenuse of a right triangle? (Answer y/n)"))
c = max(x,y)
a = min(x,y)
b = 0
b = math.sqrt(c**2 - a**2)

if answer == ("y"):
    print(f"The missing side of your triangle is {b}")
    exit()
if answer == ("n"):
    print("Ok I cant really help you then")
    exit()

print("Invalid input")