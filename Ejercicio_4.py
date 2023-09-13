#Vamos a realizar un código quee por pantalla haga un cálculo de variables que nos permita sumar, restar y hacer operaciones para buscar al final un resultado de cada operación y a su vez crear una tabla de la verdad
#y cada una de las operaciones usando "bool" o usando and y or.
print("Este programa no se debe hacer por ChatGPT, el que lo haga le bajo nota")

a = input("Ingrese un número en pantalla: ")
b = input("Ingrese un número mayor al anterior: ")


a = int(a)
b = int(b)


print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#Tabla del And
print("Tabla de la verdad todo lo relacionado con And")
print(str(a==a) + " And " + str(b==b) + " -----> " + str(a==a))
print(str(a==a) + " And " + str(a==b) + " -----> " + str(a==b))
print(str(a==b) + " And " + str(a==a) + " -----> " + str(a==b))
print(str(a==b) + " And " + str(a==b) + "-----> " + str(a==b))
print("                     ")

#Tabla del Or
print("Tabla de la verdad todo lo relacionado con Or")
print(str(a==a) + " And " + str(b==b) + " -----> " + str(a==a))
print(str(a==a) + " And " + str(a==b) + " -----> " + str(a==a))
print(str(a==b) + " And " + str(a==a) + " -----> " + str(a==a))
print(str(a==b) + " And " + str(a==b) + "-----> " + str(a==b))

#Ejercicio de tabla de verdad ejecutado con boolean

a = input("Ingrese un número en pantalla: ")
b = input("Ingrese un número mayor al anterior: ")

a = str(a)
b = str(b)


print(bool(a==a))
print(bool(a==b))
print(bool(b==a))
print(bool(b==b))


print("                    ")


print(bool(a!=a))
print(bool(a!=b))
print(bool(b!=a))
print(bool(b!=b))

