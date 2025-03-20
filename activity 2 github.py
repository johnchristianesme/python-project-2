# A program to demonstrate Python keywords in a real-world context
# Created by [John Christian Esmejarda] - March 2025

# Importing modules
import os.path as path  # 'as' keyword for aliasing
from math import sqrt  # 'from' and 'import' keywords

# Global variable to track user attempts
global_attempts = 0  # 'global' keyword

# Class to represent a bank account
class BankAccount:  # 'class' keyword
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")  # 'raise' keyword
        self.balance -= amount
        return self.balance

# Function to calculate the square root of a number
def calculate_sqrt(num):  # 'def' keyword
    assert num >= 0, "Number must be non-negative"  # 'assert' keyword
    return sqrt(num)

# Lambda function to calculate the area of a circle
circle_area = lambda r: 3.14 * r ** 2  # 'lambda' keyword

# Main program logic
def main():
    # 'if', 'elif', 'else' keywords
    if global_attempts == 0:  # 'if' keyword
        print("Welcome! This is your first attempt.")
    elif global_attempts == 1:  # 'elif' keyword
        print("Welcome back! This is your second attempt.")
    else:
        print("Welcome back! You've tried this multiple times.")  # 'else' keyword

    # 'for' loop with 'in' and 'break' keywords
    print("Counting to 5:")
    for i in range(10):  # 'for' and 'in' keywords
        if i == 5:
            break  # 'break' keyword
        print(i, end=" ")

    print("\n")

    # 'while' loop with 'continue' keyword
    print("Skipping number 3:")
    counter = 0
    while counter < 5:  # 'while' keyword
        counter += 1
        if counter == 3:
            continue  # 'continue' keyword
        print(counter, end=" ")

    print("\n")

    # 'try', 'except', 'finally' keywords
    try:
        result = calculate_sqrt(-1)  # This will raise an AssertionError
    except AssertionError as e:  # 'except' and 'as' keywords
        print(f"Error: {e}")
    finally:  # 'finally' keyword
        print("Square root calculation attempted")

    # 'with' keyword for file handling
    with open("output.txt", "w") as file:  # 'with' keyword
        file.write("This is a test file.")

    # 'del' keyword
    my_list = [10, 20, 30, 40, 50]
    del my_list[2]  # 'del' keyword
    print("List after deleting the third element:", my_list)

    # 'nonlocal' keyword
    def outer_function():
        x = 100

        def inner_function():
            nonlocal x  # 'nonlocal' keyword
            x = 200

        inner_function()
        print("Nonlocal x after modification:", x)

    outer_function()

    # 'yield' keyword for generator
    def generate_fibonacci(limit):  # 'def' keyword
        a, b = 0, 1
        while a < limit:
            yield a  # 'yield' keyword
            a, b = b, a + b

    print("Fibonacci sequence up to 20:")
    for num in generate_fibonacci(20):  # 'for' and 'in' keywords
        print(num, end=" ")

    print("\n")

    # 'None' keyword
    def no_return_function():
        pass  # 'pass' keyword

    result = no_return_function()
    print("Function returned:", result)  # 'None' keyword

    # 'True' and 'False' keywords
    is_raining = True  # 'True' keyword
    is_sunny = False  # 'False' keyword
    print("Is it raining?", is_raining)
    print("Is it sunny?", is_sunny)

    # 'is' keyword
    list1 = [1, 2, 3]
    list2 = list1
    print("Are list1 and list2 the same object?", list1 is list2)  # 'is' keyword

    # 'not' and 'or' keywords
    if not is_sunny or is_raining:  # 'not' and 'or' keywords
        print("Better bring an umbrella!")

    # 'return' keyword
    def add_numbers(a, b):
        return a + b  # 'return' keyword

    print("Sum of 7 and 8:", add_numbers(7, 8))

    # 'raise' keyword
    def check_age(age):
        if age < 18:
            raise ValueError("You must be at least 18 years old")  # 'raise' keyword
        return "Access granted"

    try:
        print(check_age(16))
    except ValueError as e:
        print(f"Error: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()