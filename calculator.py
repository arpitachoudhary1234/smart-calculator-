
# Functions

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a,b):
    return a/b

def modulus(a,b):
    return a%b

# Calculator

while True:
    print("------- SMART CALCULATOR -------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice in (1, 2, 3, 4, 5):
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))

        if choice == 1:
            result = add(n1, n2)
            print("Result:", result)

        elif choice == 2:
            result = subtraction(n1, n2)
            print("Result:", result)

        elif choice == 3:
            result = multiplication(n1, n2)
            print("Result:", result)

        elif choice == 4:
            if n2 != 0:
                print("Result:", n1 / n2)
            else:
                print("Cannot divide by zero")

        elif choice == 5:
            print("Result:", n1 % n2)

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
