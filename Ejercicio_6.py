print("<--------------------------------------- Inicio del programa ---------------------------------------->")

Edad1 = int(input("Ingresa tu edad: "))

if Edad1 < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

CorreoUsuario = str(input("ingresa tu correo electronico: "))
NumeroUsuario = int(input("Ingresa tu número de telefono: "))

print("<--------------------------------------- Modulo de seguridad ----------------------------------------->")

#Aca el usuario una vez se estlablece si es mayor de edad, le vamos a solicitar una contrasena

print("Tu contraseña fue enviada a tu correo")
print("Si no te llegó al correo, revisa tus mensajes de telefono")

ClaveMayorEdad = "c0n7r453ñ4"
password = input("Ingresa la contraseña que fue enviada a tu correo: ")

if ClaveMayorEdad == password.lower():
    print("Contraseña correcta")
else:
    print("La contraseña es incorrecta")


print("<-------------------------------------- Modulo 3 de interacción -------------------------------------->")

print("Escribe tu frase o palabra de seguridad para seguir adelante en la autenticación")

PalabraSeguridad = "EsperoQueSalgaMiPrograma"
Frase = input(" Ingresa  una frase: ")

if PalabraSeguridad == Frase:
    print("Se ha autenticado correctamente")
else:
    print("No se ha podido autenticar")

#Si se desea reemplazar la contraseña, solicite al usuario escribir en diferentes letras o núnemos para
#la nueva contraseña o simplemente solicite un parametro de autenticación


FraseNueva = input("Introduzca una frase nueva: ")

Palabraseguridad = FraseNueva
