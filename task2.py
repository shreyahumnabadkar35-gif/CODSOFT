def calculator():
    print("----Simple Calculator-----")

    while True:
        print("\n1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Choose from (1-5): ")

        if choice == '5':
            print("Calculator closed")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice")
            continue

        no1 = float(input("Enter value of  first number = "))
        no2 = float(input("Enter value of second number = "))

        if choice == '1':
            print("Addition =", no1+no2)

        elif choice == '2':
            print("Subtraction =", no1-no2)

        elif choice == '3':
            print("Multiplication =", no1*no2)

        elif choice == '4':
            if no2 == 0:
                print("Cannot divide by 0")

            else:
                print("Division =", no1/no2)
calculator()
