while True:
    print("\n📟 Simple Calculator")
    print("Select Operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit\n")

    choice = int(input("Enter your choice (1/2/3/4/5): "))

    if choice == 5:
        print("👋 Exiting the calculator. Goodbye!")
        break

    if choice not in [1, 2, 3, 4]:
        print("❌ Invalid choice. Please select 1, 2, 3, or 4.\n")
        continue

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.\n")
        continue

    if choice == 1:
        print("Result:", num1 + num2)
    elif choice == 2:
        print("Result:", num1 - num2)
    elif choice == 3:
        print("Result:", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("❌ Error: Division by zero.")