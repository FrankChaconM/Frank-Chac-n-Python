#Esta es una programación para el registro o inscripción a una clase o actividad
print("¡Bienvenid@, es un gusto verte aquí!")                       #Bienvenida

Nombres_Ins_bal = []                         #Esta lista contiene el nombre de la persona que se inscribe
Nombres_Ins_fut = []                         #Esta lista contiene el nombre de la persona que se inscribe
Nombres_Ins_vol = []                         #Esta lista contiene el nombre de la persona que se inscribe

Docs_Ins_Total =[]

Contrasenas_Ins_bal = []                     #Esta lista contiene una contraseña hecha por la persona para poder ingresar
Contrasenas_Ins_fut = []                     #Esta lista contiene una contraseña hecha por la persona para poder ingresar
Contrasenas_Ins_vol = []                     #Esta lista contiene una contraseña hecha por la persona para poder ingresar

Act_1 = ["baloncesto"]
Act_2 = ["futbol"]
Act_3 = ["voleibol"]

Cupos_bal = 3                                #Cantidad de cupos para la actividad
Cupos_fut = 3                                #Cantidad de cupos para la actividad
Cupos_vol = 3                                #Cantidad de cupos para la actividad

while True:
    Act_Selec = str(input("Elige una actividad entre: baloncesto, futbol, voleibol. O escribe 'fin' para terminar: "))
    if Act_Selec in Act_1:
        while True:
            if Cupos_bal <= 0:
                print("No hay más cupos para baloncesto.")
                break                                                          
            Nueva_Ins_bal = input("Ingresa tu nombre y apellido (o escribe 'salir' para voler a seleccionar actividad): ") 
            if Nueva_Ins_bal == 'salir':
                    break
            Doc_Ins = str(input("Ingresa tu documento: "))
            if Doc_Ins in Docs_Ins_Total:
                print("Ya estás inscrit@ en esta u otra actividad.")
            else:     
                for i in range(3):
                    Contrasena_Nuevo_Ins_bal = str(input("Ingresa una contraseña de 4 digitos: "))
                    if len(Contrasena_Nuevo_Ins_bal) < 4:
                        print("La contraseña debe tener al menos 4 números.")
                    elif len(Contrasena_Nuevo_Ins_bal) > 4:
                        print("La contraseña debe tener no más de 4 números.")
                    else:
                        if Contrasena_Nuevo_Ins_bal in Contrasenas_Ins_bal:
                            print("Contraseña no disponible.")                                            
                        else: 
                            Nombres_Ins_bal.append(Nueva_Ins_bal)
                            Contrasenas_Ins_bal.append(Contrasena_Nuevo_Ins_bal)
                            Docs_Ins_Total.append(Doc_Ins)
                            Cupos_bal = Cupos_bal - 1
                            break
    elif Act_Selec in Act_2:
        while True:         
            if Cupos_fut <= 0:
                print("No hay más cupos para futbol.")
                break                                                 
            Nueva_Ins_fut = input("Ingresa tu nombre y apellido (o escribe 'salir' para voler a seleccionar actividad): ")      
            if Nueva_Ins_fut == 'salir':
                break
            Doc_Ins = str(input("Ingresa tu documento: "))
            if Doc_Ins in Docs_Ins_Total:
                print("Ya estás inscrit@ en esta u otra actividad.")
            else:
                for i in range (3):
                    Contrasena_Nuevo_Ins_fut = str(input("Ingresa una contraseña de 4 digitos: "))
                    if len(Contrasena_Nuevo_Ins_fut) < 4:
                        print("La contraseña debe tener al menos 4 números.")
                    elif len(Contrasena_Nuevo_Ins_fut) > 4:
                        print("La contraseña debe tener no más de 4 números.")
                    else:
                        if Contrasena_Nuevo_Ins_fut in Contrasenas_Ins_fut:
                            print("Contraseña no disponible.")                                            
                        else: 
                            Nombres_Ins_fut.append(Nueva_Ins_fut)
                            Contrasenas_Ins_fut.append(Contrasena_Nuevo_Ins_fut)
                            Docs_Ins_Total.append(Doc_Ins)
                            Cupos_fut = Cupos_fut - 1
                            break
    elif Act_Selec in Act_3:
        while True:
            if Cupos_vol <= 0:
                print("No hay más cupos para voleibol.")
                break                                                          
            Nueva_Ins_vol = input("Ingresa tu nombre y apellido (o escribe 'salir' para voler a seleccionar actividad): ")      
            if Nueva_Ins_vol == 'salir':
                break
            Doc_Ins = str(input("Ingresa tu documento: "))
            if Doc_Ins in Docs_Ins_Total:
                print("Ya estás inscrit@ en esta u otra actividad.")
            else:
                for i in range (3):
                    Contrasena_Nuevo_Ins_vol = str(input("Ingresa una contraseña de 4 digitos: "))
                    if len(Contrasena_Nuevo_Ins_vol) < 4:
                        print("La contraseña debe tener al menos 4 números.")
                    elif len(Contrasena_Nuevo_Ins_vol) > 4:
                        print("La contraseña debe tener no más de 4 números.")
                    else:
                        if Contrasena_Nuevo_Ins_vol in Contrasenas_Ins_vol:
                            print("Contraseña no disponible.")                                            
                        else: 
                            Nombres_Ins_vol.append(Nueva_Ins_vol)
                            Contrasenas_Ins_vol.append(Contrasena_Nuevo_Ins_vol)
                            Docs_Ins_Total.append(Doc_Ins)
                            Cupos_vol = Cupos_vol - 1
                            break
    elif Act_Selec == "fin":
        print("Hasta luego.")
    else:
        print("No tenemos esa actividad.")
    if Act_Selec == "fin":
        break

print("Los inscritos para baloncesto son: ", Nombres_Ins_bal)
print("Los inscritos para baloncesto son: ", Nombres_Ins_fut)
print("Los inscritos para baloncesto son: ", Nombres_Ins_vol)
