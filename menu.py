from controllers import form_agregar_cita, form_editar_cita, buscar_todos
import os

while True:
    os.system("cls")

    print("Bienvenido al MENÚ DE OPCIONES de CARWIN \n" \
    "¿Qué desea hacer hoy? \n" \
    "--------------------------------\n"\
    "1- Agregar cita \n" \
    "2- Editar cita \n" \
    "3- Ver todas las citas \n" \
    "0- salir")

    opt = int(input("Ingrese opción -> "))

    while opt < 0 or opt > 3:
        opt = int(input("Ingrese opción valida (0-3) -> "))


    if opt == 1:
        # Agregar cita
        os.system("cls")
        print("==== Formulario De Agendacion de Citas ====")
        form_agregar_cita()
        
        print("===========================")
        salir = input("Para continuar, presione ENTER ")
        # Poner retraso antes de limpiar pantalla, para mostrar mesaje de confirmacion de la cita
    
    elif opt == 2:
        # editar cita
        os.system("cls")
        print("==== Formulario para modificar citas ====")

        form_editar_cita()
        print("===============================")

        salir = input("Para volver, presione ENTER ")

    elif opt == 3:
        # mostrar todos los registros
        os.system("cls")
        print("Todos los registros de citas")
        buscar_todos()

        print("===========================")
        salir = input("Para volver, presione ENTER ")


    elif opt == 0:
        # salir
        print("Saliendo del menú...")
        exit()



