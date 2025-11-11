from main import form_agregar_cita, editar_cita
import os

while True:
    os.system("cls")

    print("Bienvenido al MENÚ DE OPCIONES de CARWIN \n" \
    "¿Qué desea hacer hoy? \n" \
    "--------------------------------\n"\
    "1- Agregar cita \n" \
    "2- Editar cita \n" \
    "0- salir")

    opt = int(input("Ingrese opción -> "))
    while opt < 0 or opt > 2:
        opt = int(input("Ingrese opción -> "))

    if opt == 1:
        # Agregar cita
        os.system("cls")
        print("==== Formulario De Agendacion de Citas ====")
        form_agregar_cita()
        # Poner retraso antes de limpiar pantalla, para mostrar mesaje de confirmacion de la cita
    
    elif opt == 2:
        # editar cita
        os.system("cls")
        print("==== Formulario para modificar citas ====")
        editar_cita()

    elif opt == 0:
        # salir
        print("Saliendo del menú...")
        break



