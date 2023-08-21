num1 = float(input("Primer numero: "))
operator = input("Operacion (+, -, *, /): ")
num2 = float(input("Segundo numero: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print("Resultado:", result)

