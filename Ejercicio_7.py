print("Tipo de programa que incluya un ciclo")

print("----------------- Inicio del ciclo -------------------")

for i in range(10):
    print(i**2)

print("Finalice el ciclo")

#En el programa que vamos a realizar tiene como finalidad realizar un ciclo en donde le pida al usuario ingresar hasta tres veces un número, en este caso la edad,
#y cuando genere la variable corriente ejecute en pantalla la siguiente acción, por ejemplo: digita tu número de cédula, 3. Digite si desea saber el número de silla donde fue asignado

print("Admisión personas")

#Nombre = str(input("Ingresa tu nombre: "))
#Edad = int(input("Ingresa tu edad: "))
#Identificacion = float(input("Ingresa tu identificación: "))
#Ubicacion = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
CantidadSillas = 5

#ListaEdades = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#if Edad >= 18:
#    print("Está permitido su ingreso")
#    for i in CantidadSillas:
#        if Edad in ListaEdades:
#            print("Tendrá su silla lo más pronto posible")
#        else:
#            print("Espere para poder tener su silla")
#else:
#    print("Usted no puede ingresar")


while (CantidadSillas > 0):
    Edad = int(input("Ingrese su edad: "))
    if Edad >= 18 and Edad <= 30:
        print("Usted puede ingresar y le asignaremos de inmediato")
        CantidadSillas = CantidadSillas - 1
    elif Edad >= 31:
        print("Usted puede ingresar, espere un momento para signar su silla")
        CantidadSillas = CantidadSillas - 1
    else:
        print("Usted no puede ingresar")

if CantidadSillas == 0:
    print("No hay más cupos, lo sentimos")