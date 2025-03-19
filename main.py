def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Division by 0 not allowed"
    return num1 / num2

def main():
    user_choice = input("Enter an operation to perform ( + , - , * , / ) separated by spaces: ")
    num1, operator, num2 = user_choice.split(" ")
    num1, num2 = float(num1), float(num2)
    
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator in operations:
        result = operations[operator](num1, num2)
        print("Result:", result)
    else:
        print("Invalid operator")

main()
