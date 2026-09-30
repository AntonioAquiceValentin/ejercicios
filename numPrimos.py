#Determina si un número es primo usando for con condicionales anidadas.

#Los numeros primos solo pueden ser divididos entre 1 y entre si mismos.

#Pedimos al usuario ingresar un numero.
 #2
num = int(input("Ingrese un numero: "))
contador = 0

for i in range(1,num+1):
        #2%1 == 0 o 2%2 == 0   
    if num%i == 0:
        contador = contador + 1
if contador > 2:
        print ("no es primo")
else:
    
        print ("es primo")
