class Calculator:
    def calculate(self, expression):
        try:
            result = eval(expression)

            if result == int(result):
                result = int(result)

            return result
        except ZeroDivisionError:
            return "Tolol ngabagi make nol"
        except Exception:
            return "Naon any"
        

def main():
    calc = Calculator()

    print("==== Rlly Simple Calc ====")
    print("Tulis we")
    print("'exit' we mun atos mah")

    while True:
        expression = input("Baraha sok: ")

        if expression.lower() == "exit":
            print("Gaje tolol")
            break

        print("Jadi: ", calc.calculate(expression))

if __name__ == "__main__":
    main()