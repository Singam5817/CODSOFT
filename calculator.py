def calculate_result():
    """
    Designs a simple calculator that performs basic arithmetic operations.
    """
    print("========================")
    print("  Simple Calculator App ")
    print("========================")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Error: Please enter valid numerical digits.")
        return

    print("\nAvailable operations: (+, -, *, /)")
    operation = input("Enter your choice of operation: ")

    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("\n❌ Error: Division by zero is not allowed.")
            return
    else:
        print("\n❌ Error: Invalid operation choice. Please use +, -, *, or /.")
        return

    print("\n--- Result ---")
    print(f"{num1} {operation} {num2} = {result}")
    print("--------------")


if __name__ == "__main__":
    calculate_result()