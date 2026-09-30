#Pide contraseña con while; máximo 3 intentos,se bloquea si falla.

#Pedir al usuario ingresar la contraseña
Password = input("Ingrese su contraseña: ") 

contador  = 1

#Cuenta el numero de veces que intenta escribir la contraseña.
while contador <= 3:
    if Password == "contraseña": #la contraseña seria contraseña
        print("Acceso concedido")
        break
    
#Si la contraseña es incorrrecta entonces pedira volver a escribirla.
    else:        
        print("Datos incorrectos, vuelva a escribir su contraseña: ")
        if contador == 3:
            print("excediste el maximo de intentos, acceso bloqueado")
        contador = contador + 1