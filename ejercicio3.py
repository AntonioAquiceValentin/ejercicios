
#calculadora con diagnostico

#Números decimales de entrada
peso = float(input("Ingrese su peso en kilogramos: "))
talla = float(input("Ingrese su talla en metros: "))

#Aplicando formula IMC
imc = peso / (talla ** 2)


if imc < 18.5:
    print("Diagnóstico: Bajo peso")
elif imc < 25:
    print("Diagnóstico: Normal")
elif imc < 30:
    print("Diagnóstico: Sobrepeso")
elif imc < 35:
    print("Diagnóstico: Obesidad I")
elif imc < 40:
    print("Diagnóstico: Obesidad II")
else:
    print("Diagnóstico: Obesidad III")