# define the calculator function
def calculator():
    print("Welcome to the Calculator Program!")
    print("Please enter two numbers:")

    # prompt the user for the first number
    num1 = float(input("First number: "))

    # prompt the user for the second number
    num2 = float(input("Second number: "))

    # prompt the user for the operation to perform
    op = input("Operation (+, -, *, /): ")

    # perform the operation and print the result
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: division by zero")
            return
        else:
            result = num1 / num2
    else:
        print("Error: invalid operation")
        return

    print(f"{num1} {op} {num2} = {result}")

# call the calculator function
calculator()
