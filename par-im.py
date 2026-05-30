num = int(input("Ingresa un número entero: "))

if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

if num > 0:
    print("El número es positivo")
elif num == 0:
    print("El número es cero")
else:
    print("El número es negativo")