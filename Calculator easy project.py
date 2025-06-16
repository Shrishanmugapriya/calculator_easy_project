def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    else:
        return x / y

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (×)")
    print("4. Divide (÷)")

    while True:
        choice = input("Select operation (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Calculator exited.")
            break

        if choice not in {'1', '2', '3', '4'}:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input: Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '×'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '÷'

        print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()
