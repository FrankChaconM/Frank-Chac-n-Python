#Hagamos un ejercicio en donde el usuario ingresa una variable numérica y por medio de una secuencia lógica me permita validar si un resultado es correcto.

Num1 = float(input("Escribe un número: "))


if Num1 == 40:
    print("¡Acertaste el número!")
elif Num1 < 40:
    print("No acertaste en este intento, prueba un número más alto que " + str(Num1))
else:
    print("No acertaste esta vez, prueba un número más bajo que " + str(Num1))
