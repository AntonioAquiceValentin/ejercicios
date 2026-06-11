#Del 1 al 50: Fizz (÷3), Buzz (÷5), FizzBuzz (÷ambos), o el número.

for i in range (1,51):

#Se pide ingresar un numero entero del 1 al 50:
    i = int(input("Ingrese un numero entero de 1 al 50: "))

    if i > 50 or i<1:
        print("Numero ingresado fuera de rango")    
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)