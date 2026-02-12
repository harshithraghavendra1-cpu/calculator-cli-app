def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error:Division by Zero not Allowed"
    return a/b
while True:
    print("\n---simple CLI calculator-----")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Exiting calculator. Thank you.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    if choice == "1":
        print("Result:", add(num1, num2))

    elif choice == "2":
        print("Result:", subtract(num1, num2))

    elif choice == "3":
        print("Result:", multiply(num1, num2))

    elif choice == "4":
        print("Result:", divide(num1, num2))
