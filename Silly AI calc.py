class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


def main():
    calc = Calculator()
    
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "5":
            print("Goodbye! 👋")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
            if choice == "1":
                result = calc.add(num1, num2)
            elif choice == "2":
                result = calc.subtract(num1, num2)
            elif choice == "3":
                result = calc.multiply(num1, num2)
            elif choice == "4":
                result = calc.divide(num1, num2)
                if isinstance(result, str):  # error message from divide
                    print(result)
                    continue
            
            # 🔑 Remove decimal point if not needed
            if result == int(result):
                result = int(result)
            
            print("Result:", result)
        else:
            print("Invalid choice! Please choose 1-5.")


if __name__ == "__main__":
    main()
