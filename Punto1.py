def operación(a, b, signo):
    if signo == "+":
        return a + b
    elif signo == "-":
        return a - b
    elif signo == "*":
        return a * b
    elif signo == "/":
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
    else:
        return "Operador no válido"

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
signo = input("Ingrese la operación (+, -, *, /): ")

resultado = operación(a, b, signo)
print(resultado)
