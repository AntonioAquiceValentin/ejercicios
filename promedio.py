#Ingresar 3 notas de un estudiante (escala 0-20). Calcular el
#promedio y mostrar si el alumno está Aprobado (≥11) o
#Desaprobado (<11).

nota1 = float(input("Ingrese nota: "))
nota2 = float(input("Ingrese nota: "))
nota3 = float(input("Ingrese nota: "))
#Sacar promedio de las 3 notas
promedio = (nota1 + nota2 + nota3) / 3
#mostrar si el alumno esta aprobado o no
if promedio >20 or promedio <0:
    print(f"error ")
elif promedio >=11:
    print(f"Aprobado")-15
else:
    print(f"desaprobado")
