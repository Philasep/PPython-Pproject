import math
welcome = "Welcome to Phila's Calculator"
print(welcome.center(20))
while True:
    print("\n Choose an option")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    choice = input("Choose option: ")

    if choice == '7':
        print("Goodbye!")
        break

    if choice == '6':
        num = float(input("Enter number: "))
        print("Result:", math.sqrt(num))

    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", num1 + num2)

        elif choice == '2':
            print("Result:", num1 - num2)

        elif choice == '3':
            print("Result:", num1 * num2)

        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error! Cannot divide by zero.")

        elif choice == '5':
            print("Result:", num1 ** num2)

        else:
            print("Invalid choice")