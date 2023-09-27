import Proyecto                                          #Conecta el primer archivo del proyecto

Inscripciones_bal = len(Proyecto.Contrasenas_Ins_bal)
Inscripciones_fut = len(Proyecto.Contrasenas_Ins_fut)
Inscripciones_vol = len(Proyecto.Contrasenas_Ins_vol)

while True:
    Act_ing = str(input("Ingresa la actividad a la que deseas ingresar o escribe 'terminar' para acabar el ingreso: "))
    if Act_ing == "baloncesto":
        if Inscripciones_bal == 0:
            print("Ya ingresaron todos los inscritos a baloncesto")
        while Inscripciones_bal > 0:
            Contrasena_ingreso = str(input("Ingresa tu contraseña para ingresar o escribe 'volver' para regresar: "))
            if Contrasena_ingreso in Proyecto.Contrasenas_Ins_bal:
                print("Puedes ingresar a la sesión de hoy.")       
                Proyecto.Contrasenas_Ins_bal.remove(Contrasena_ingreso)
                Inscripciones_bal = Inscripciones_bal - 1
            else:
                print("Contraseña incorrecta.")
            if Contrasena_ingreso == "volver":
                break
    elif Act_ing == "futbol":
        if Inscripciones_fut == 0:
            print("Ya ingresaron todos los inscritos a futbol")
        while Inscripciones_fut > 0:
            Contrasena_ingreso = str(input("Ingresa tu contraseña para ingresar o escribe 'volver' para regresar: "))
            if Contrasena_ingreso in Proyecto.Contrasenas_Ins_fut:
                print("Puedes ingresar a la sesión de hoy.")       
                Proyecto.Contrasenas_Ins_fut.remove(Contrasena_ingreso)
                Inscripciones_fut = Inscripciones_fut - 1
            else:
                print("Contraseña incorrecta.")
            if Contrasena_ingreso == "volver":
                break
    elif Act_ing == "voleibol":
        if Inscripciones_vol == 0:
            print("Ya ingresaron todos los inscritos a voleibol")
        while Inscripciones_vol > 0:
            Contrasena_ingreso = str(input("Ingresa tu contraseña para ingresar o escribe 'volver' para regresar: "))
            if Contrasena_ingreso in Proyecto.Contrasenas_Ins_vol:
                print("Puedes ingresar a la sesión de hoy.")       
                Proyecto.Contrasenas_Ins_vol.remove(Contrasena_ingreso)
                Inscripciones_vol = Inscripciones_vol - 1
            else:
                print("Contraseña incorrecta.")
            if Contrasena_ingreso == "volver":
                break
    if Act_ing == "terminar":
        break
    if Inscripciones_bal == 0 and Inscripciones_fut == 0 and Inscripciones_vol == 0:
        break
    