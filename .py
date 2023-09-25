# Crear un diccionario vacío
mi_diccionario = {}

# Solicitar al usuario que ingrese datos y claves para el diccionario
while True:
    clave = input("Ingresa una clave (o escribe 'salir' para terminar): ")
    
    # Verificar si el usuario quiere salir (ignorar mayúsculas y minúsculas)
    if clave.lower() == 'salir':
        break
    
    valor = input("Ingresa un valor para la clave '" + clave + "': ")
    
    # Agregar el par clave-valor al diccionario
    mi_diccionario[clave] = valor

# Imprimir el diccionario resultante
print("Tu diccionario ingresado es:", mi_diccionario)