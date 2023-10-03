##Simple Calculator Function
#Create a Python function called calculator that takes three arguments: two numbers and an operator (e.g., "+", "-", "*", "/"). The function should perform the corresponding arithmetic operation on the two numbers and return the result. Test your function with various arithmetic operations.

num1_str = input("Number 1: ")
num2_str = input("Number 2: ")
operator = input("Select operator: ")

try:
    num1 = float(num1_str)
    num2 = float(num2_str)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
    exit(1)

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num1 or num2 != 0: 
            return num1 / num2
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operator"

result = calculator(num1, num2, operator)
print("Result: ", result)