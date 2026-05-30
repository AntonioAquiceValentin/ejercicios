#Ingresar 3 notas de un estudiante (escala 0-20). Calcular el
#promedio y mostrar si el alumno está Aprobado (≥11) o
#Desaprobado (<11).

nota1 = float(input("Ingrese nota: "))
nota2 = float(input("Ingrese nota: "))
nota3 = float(input("Ingrese nota: "))

#Filtro que evita añadir una nota negativa o superior a 20

if nota1<0 or nota1>20 or nota2<0 or nota2>20 or nota3<0 or nota3>20:
    print("Error, ingresa una nota del 0 al 20.")
else:
    promedio = (nota1 + nota2 + nota3) / 3
    promedio = round(promedio,1)

#mostrar si el alumno esta aprobado o no

    if promedio >=11:
        print(f"¡Felicitaciones! Aprobaste con {promedio}")
    else:
        print(f"¡Esfuerzate más! Desaprobaste {promedio}")
