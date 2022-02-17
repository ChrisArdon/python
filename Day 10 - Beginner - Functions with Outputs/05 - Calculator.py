#Calculator
from art import logo
#Add
def add(n1,n2):
    return n1 + n2

#Substract
def subtract(n1,n2):
    return n1 - n2

#Multiply 
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1/n2

#This dictionary will fuction as the means to call the fuctions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    #Inputs
    num1 = float(input("What's the first number?: "))
    
    #Showing the symbols of each operation
    for symbol in operations:
        print(symbol)
    should_continue = True
    
    #Loop to continue calculating if the user chose yes
    while should_continue:    
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        #Chosing the calculation from the dictionary based on the operation symbol
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            #num1 becomes the previus answer
            num1 = answer
        else:
            should_continue = False
            calculator() #Recurssion

calculator()