#Esta es una programación para el registro o inscripción a una clase o actividad

print("¡Bienvenido! Necesitamos unos datos tuyos, por favor ingresalos a continuación.")  #Bienvenida

Cupos = 3                                #Cantidad de cupos para la actividad
Nombres_Ins = []                         #Esta lista contiene el nombre de la persona que se inscribe
Contrasenas_Ins = []                     #Esta lista contiene una contraseña hecha por la persona para poder ingresar

for i in range(1000000000000000000):
    Nueva_Ins = input("Ingresa tu nombre y apellido (o escribe 'salir' para terminar): ")
    if Nueva_Ins == 'salir':
        break
    Contrasena_Nuevo_Ins = int(input("Ingresa una contraseña de 4 digitos: "))
    if Contrasena_Nuevo_Ins in Contrasenas_Ins:
        print("Contraseña no disponible.")
    else: 
        Nombres_Ins.append(Nueva_Ins)
        Contrasenas_Ins.append(Contrasena_Nuevo_Ins)
        Cupos = Cupos - 1
    if Cupos == 0:
        print("No hay más cupos.")
        break

print("Los inscritos son: ", Nombres_Ins)
#Nuevo_Est = input(str("Ingresa tu nombre: "))  #Variable del estudiante nuevo
print(Contrasenas_Ins)
Contrasena_ingreso = int(input("Ingresa tu contraseña para ingresar:"))

Cupos = 3

while Cupos > 0:
    if Contrasena_ingreso in Contrasenas_Ins:
        print("Puedes ingresar a la sesión de hoy.")
        Contrasenas_Ins.remove(Contrasena_ingreso)
        Cupos = Cupos - 1
    else:
        print("Contraseña incorrecta.")
        break