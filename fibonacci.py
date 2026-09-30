#Genera todos los números Fibonacci menores que N usando while + condicionales

#La secuencia de Fibonacci es una serie matemática infinita donde cada número 
# se obtiene sumando los dos números anteriores. La secuencia comienza tradicionalmente
#  con 0 y 1:\(0,1,1,2,3,5,8,13,21,34,55,89,144,233...\)

a, b = 0, 1

while b < 15:
    print (b)
    c = a + b
    a = b
    b = c