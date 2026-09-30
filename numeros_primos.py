#Ejercicio 5: Números primos
numero = int(input("Ingresa un número: "))

#Asumimos que el número es primo, por eso ponemos true
es_primo = True

#Los números menores que 2 no son primos
if numero < 2:
    es_primo = False
else:
    #Recorremos posibles divisores desde 2 hasta numero - 1
    for i in range(2, numero):

        #Si el residuo es 0, significa que sí divide exacto
        if numero % i == 0:
            es_primo = False

            #Ya no seguimos buscando
            break

#Mostramos el resultado final
if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")