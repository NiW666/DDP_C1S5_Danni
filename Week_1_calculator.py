

def add(num1, num2):
    return num1+num2

def substract(num1, num2):
    return num1-num2

def mutiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    if num2 == 0:
        return "Error"
    else:
        return num1/num2   
    
def calculator():
    while True:
        print("Select an operation:")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")

        choice = input()
        if choice == "1":
            num1=int(input("Enter number1:"))
            num2=int(input("Enter number2:"))
            print(add(num1, num2))

        if choice == "2":
            num1=int(input("Enter number1:"))
            num2=int(input("Enter number2:"))
            print(substract(num1, num2))

        if choice == "3":
            num1=int(input("Enter number1:"))
            num2=int(input("Enter number2:"))
            print(mutiply(num1, num2))

        if choice == "4":
            num1=int(input("Enter number1:"))
            num2=int(input("Enter number2:"))
            print(divide(num1, num2))

calculator()


