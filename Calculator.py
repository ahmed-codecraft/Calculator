def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def main():
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        '5': ('Exponent (x^y)', power),
        '6': ('Modulo (x%y)', modulo)
    }

    print("--- Python Calculator ---")
    
    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("7. Exit")

        choice = input("Enter choice (1-7): ").strip()

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            name, func = operations[choice]
            result = func(num1, num2)
            print(f"Result ({name}): {result}")
        else:
            print("Invalid selection! Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()
