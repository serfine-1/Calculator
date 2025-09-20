# 🎉 Welcome to the Fun Calculator! 🎉
# Menu-driven calculator that performs only the chosen operation and repeats until exit

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ That's not a valid number. Try again.")

def calculator():
    while True:
        print("\nChoose an operation:")
        print("1) Addition (+)")
        print("2) Subtraction (-)")
        print("3) Multiplication (*)")
        print("4) Division (/)")
        print("5) Exponentiation (^)")
        print("6) Modulus (%)")
        print("7) Square Root (√)")
        print("8) Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("👋 Goodbye!")
            break

        if choice not in {"1","2","3","4","5","6","7"}:
            print("❌ Invalid choice. Please choose 1-8.")
            continue

        if choice == "7":
            num = get_number("Enter the number: ")
            if num < 0:
                print("⚠️ Error: Cannot take the square root of a negative number.")
            else:
                print(f"✅ √{num} = {num ** 0.5}")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            print(f"✅ {num1} + {num2} = {num1 + num2}")
        elif choice == "2":
            print(f"✅ {num1} - {num2} = {num1 - num2}")
        elif choice == "3":
            print(f"✅ {num1} * {num2} = {num1 * num2}")
        elif choice == "4":
            if num2 == 0:
                print("⚠️ Error: Division by zero is not allowed.")
            else:
                print(f"✅ {num1} / {num2} = {num1 / num2}")
        elif choice == "5":
            print(f"✅ {num1} ^ {num2} = {num1 ** num2}")
        elif choice == "6":
            if num2 == 0:
                print("⚠️ Error: Modulus by zero is not allowed.")
            else:
                print(f"✅ {num1} % {num2} = {num1 % num2}")

if __name__ == "__main__":
    calculator()
