#Clasificar un numero
#Pedir un número real al usuario y clasificarlo en: positivo,
#negativo o cero. Además indicar si es entero o decimal.

num = float(input("Ingrese un numero: "))
#positivo, negativo o cero.
if num < 0:
    print(f"El numero {num} es negativo")
elif num > 0:
    print(f"El numero {num} es positivo")
else:
    print (f"Es cero")
if num % 1 == 0:
    print(f"El numero es entero ")
else:
    print(f"Es un numero decimal ")
    