def main():
    userChoice = input("Enter an operation to perform ( + , - , * , / ) seperated by spaces: ")
    num1,operator,num2 = userChoice.split(" ")
    print(num1, operator, num2)




def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


    
def multiplication(num1, num2):
    return(num1*num2)
    
main()
def division(num1, num2):
    if(num2 == 0):
        print("Zero Division Error")
        return "Division by 0 not allowed"
    return (num1 / num2)

main()