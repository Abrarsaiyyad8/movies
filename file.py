"""
This module provides a simple command-line calculator.
It supports basic arithmetic operations: addition, subtraction, multiplication,
and division, with error handling for invalid inputs and zero division.
"""


def calculator():
    """
    Runs an infinite loop to accept user input for mathematical operations.
    The loop breaks when the user enters 'q'.
    """
    print("--- Simple Python Calculator ---")
    print("Select operation: +, -, *, /")
    print("Enter 'q' to quit")

    while True:
        choice = input("\nEnter operator (+, -, *, /) or 'q': ").lower().strip()

        if choice == 'q':
            print("Exiting... goodbye!")
            break

        if choice in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '+':
                    print(f"Result: {num1 + num2}")
                elif choice == '-':
                    print(f"Result: {num1 - num2}")
                elif choice == '*':
                    print(f"Result: {num1 * num2}")
                elif choice == '/':
                    if num2 == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        print(f"Result: {num1 / num2}")

            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid operator! Please use +, -, *, or /.")


if __name__ == "__main__":
    calculator()