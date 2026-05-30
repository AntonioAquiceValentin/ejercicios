#Solicitar al usuario que ingrese la temperatura en grados Celsius
cel = float(input("Ingrese la temperatura en grados Celsius: "))

#Conversión de Celsius a Fahrenheit y Kelvin
fahr = (cel * 9/5) + 32
kel = cel + 273.15

#Mostrar los resultados
print(f"La temperatura en grados Fahrenheit es: {fahr:.2f}")
print(f"La temperatura en grados Kelvin es:  {kel:.2f}")