#This code allows user's to add, subtract, multiply, and divide numbers. It also includes exception handling such as Zero Division Error and Value Error.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    operation = input("Select operation:\n\t(1) Addition\n\t"
                      "(2) Subtraction\n\t(3) Multiplication\n\t"
                      "(4) Division\n\t""\n\tInput your operation here: ")
    if operation in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "1":
                print(num1, "+", num2, "=", add(num1, num2))
            elif operation == "2":
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif operation == "3":
                print(num1, "X", num2, "=", multiply(num1, num2))
            elif operation == "4":
                print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("Invalid Input!")
                print("Program only accepts integers. Please Try Again.")

        except (ValueError, ZeroDivisionError):
            print("Invalid input!")
            print("Program only accepts numbers and cannot divide by 0. Please Try Again.")

        else:
            while True:
                choice = input("Would you like to try again? (y/n) ")
                if choice == "y":
                    break
                elif choice == "n":
                    print("Thank You!")
                    exit()
                else:
                    print("Error! Invalid Input. Please input 'y' or 'n'.")

    else:
        print("Error! Program only accepts numbers 1-4.")
