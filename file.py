def calculator():
    print("--- Simple Python Calculator ---")
    print("Select operation: +, -, *, /")
    print("Enter 'q' to quit")

    while True:
        # Get user input for the operation
        choice = input("\nEnter operator (+, -, *, /) or 'q': ").lower()

        if choice == 'q':
            print("Exiting... goodbye!")
            break

        if choice in ('+', '-', '*', '/'):
            try:
                # Get the numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                # Perform the math
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