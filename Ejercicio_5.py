#Vamos a realizar secuencias con condiciones basadas en ciclos.


x = ("A")
y = ("B")
z = ("C")


#list = ["10", "L", "perro", "casa", x, y, z]

#list = [10, "gato", x, 233, 45, y, z, "carro", "moto",]

#list.append("Ean")
#list.index("Ean")
#list.remove(x)
#list.reverse()

#print(list[7])
#print(list[3:6])
#print(list * 2)

#print (list)

list1 = [10, x, y, "gato", 20, "perro", z, z, "loro", 30, 40, "pez", 68, "hamster", y]
list2 = [22, 50, "ñ"]

list1.append("rata")
#list1.clear()
list1.count(5)
list1.extend(list2)
list1.index(10)
list1.pop(4)
list1.remove("loro")
list1.reverse()

list3 = list.copy(list1)

print(list1)
print(list3)