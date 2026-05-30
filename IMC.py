peso = float(input("Ingrese su peso): "))
altura= float(input("Ingrese su altura): "))

imc = peso/(altura ** 2)

if imc < 18.5:
    print(f"Su IMC es {imc:.2f} Usted  esta en el rango de Bajo peso")
elif imc > 18.5 and imc < 24.9: 
    print(f"Su IMC es {imc:.2f} Usted  esta en el rango de Peso normal")
elif imc < 29.9: 
    print(f"Su IMC es {imc:.2f} Usted  esta en el rango de Sobrepeso")
elif imc <34.9: 
    print(f"Su IMC es {imc:.2f} Usted  esta en el rango de Obesidad Grado I")
elif imc > 39.9:
    print(f"Su IMC es {imc:.2f} Usted  esta en el rango de Obesidad Grado II")
else:
    print(f"Su IMC es {imc:.2f} Usted  esta en el rango de Obesidad Grado III")