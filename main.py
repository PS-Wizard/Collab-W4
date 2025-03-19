def main():
    userChoice = input("Enter an operation to perform ( + , - , * , / ) seperated by spaces: ")
    num1,operator,num2 = userChoice.split(" ")
    print(num1, operator, num2)

def subtract(num1, num2):
    return num1 - num2


main()

    
    
