#Importar una biblioteca 
import math

#Solictar el radio del circulo
r = float(input("Ingresa el radio del circulo: "))
area = math.pi*pow(r,2)
pe = 2*math.pi*r

#Mostrar el area y perímetro del circulo
print(f"El área del circulo es: {area:.2f}")
print(f"El perímetro del circulo es: {pe:.2f}")