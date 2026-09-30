#Dibuja una pirámide de N filas usando bucles for anidados.

#Pedir al usuario ingresar un numero
#3
n = int(input("Ingrese un numero: "))

for i in range(1,n+1):  # (1,2,3)
    for j in range(1,i+1): #1  12  123
        print(j,end="")  #utilizamos end="" para eliminar el salto de linea
    print(" ")  #utilizamos   print (" ") para que nos de un salto de linea.
   



 
   
