#Ejercicio 7: Validar contraseña
password_correcta = "python123"

#Contador de intentos fallidos
intentos_fallidos = 0

#Máximo 3 intentos
while intentos_fallidos < 3:
    password = input("Ingresa la contraseña: ")

    #Si la contraseña es correcta, entra y termina
    if password == password_correcta:
        print("Acceso permitido")
        break
    else:
        #Aumenta intentos fallidos
        intentos_fallidos += 1
        print("Contraseña incorrecta")

        #Avisa si todavía quedan intentos
        if intentos_fallidos < 3:
            print("Intenta nuevamente")

#Si falló 3 veces, se bloquea
if intentos_fallidos == 3:
    print("Cuenta bloqueada")