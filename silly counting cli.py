operator = input("Mau ak apain (+ - * /) : ")
num1 = float(input("Berapa : "))
num2 = float(input("Sama berapa : / "))

if operator == "+":
    result = num1 + num2
    print (round(result, 5))
elif operator == "-":
    result = num1 - num2
    print (round(result, 5))
elif operator == "*":
    result = num1 * num2
    print (round(result, 5))
elif operator == "/":
    result = num1 / num2
    print (round(result, 5))
else:
    print(f"{operator} teh naon ai maneh gaje ih")
