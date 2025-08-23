operator = input("Mau ak apain (+ - * /) : ")
num1 = float(input("Berapa : "))
num2 = float(input("Sama berapa :  "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2    
elif operator == "*":
    result = num1 * num2    
elif operator == "/":
    result = num1 / num2
    
print(f"anjay : {result}")
