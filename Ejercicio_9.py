#Vamos a realizar un programa que realice una tupla compuesta por diferentes tipos de datos que incluyan variables que incluyan adicionalmente que estén orientados a realizar
#diferentes acciones enfocadas en generar resultadosen esas variaciones

import random
print("Este es un programa de tuplas")

n = [(1, 4), (4, 8)]
t = [("Frank",1), (34, "hogar")]

print(n, t)

res = ()

#for n in res:
#    print(n)
#    if n == res:
#        print(res)

#Localizar dentro de una tupla la posición por un operador de referencia como:.

A = ("casa", "programa para posicionar" ,"programa para posicionar tuplas en una variable", [2, 9, 2022])

print(A[1:4])

B = ("blaco", "amarillo", "azul", [234], [3345], [88], "rojo", [1359])

print(B[0:1])
print(B[2:4])
print(B[3:9])

for A in res:
    print(A)
    if A == True:
        print("casa")