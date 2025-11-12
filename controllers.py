from models.model import Cita


def verifRut(rut):
    rut = rut.strip().replace(".","").replace("-","")
    
    if len(rut) < 2:
        return False
    
    numero = rut[:-1]
    dv = rut[-1].upper()
    
    suma = 0
    multi = 2
    
    for i in reversed(range(len(numero))):
        suma += int(numero[i]) * multi
        multi = multi + 1 if multi < 7 else 2
    
    dv_calculado = 11 - (suma % 11)
    
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 1:
        dv_calculado == 'K'
    
    return str(dv_calculado) == dv

def form_agregar_cita():
    vehiculos = ["Automovil","Motocicleta"]
    # tipo_lavado = 
    
    # cliente
    print("\n==== Datos Del Cliente ====")
    nombre_Cliente = input("Ingrese nombre del Cliente: ")
    nombre_Cliente = nombre_Cliente.capitalize()
    
    rut_Cliente=input("Ingrese Rut: ")

    # while verifRut(rut_Cliente) == False :
    #     print("RUT no valido, vuelva a ingresar")
    #     rut_Cliente=input("Ingrese Rut: ")

    fono_Cliente=input("Número De telefono: ")

    # vehiculo
    print("\n===== Datos Del Vehiculo ====")
    marca=input("Marca Del Vehiculo: ")
    # modelo_vehiculo=input(f"¿ Cual es el modelo del vehículo ?: ")
    modelo_Vehiculo=input("Modelo del vehículo: ")
    patente=input("Patente del vehículo: ")

    # fecha
    print("\nFecha De Agendacion De cita")
    fecha=input("¿Cúando desea agendar su lavado de Vehiculo? (DD-MM-YYYY): ")
    fecha_Cita = fecha.strip().replace("/","-")

    print(f"Se ha Agendado una cita para: {nombre_Cliente}, vehiculo {marca} Modelo {modelo_Vehiculo}. Para el dia {fecha_Cita}")
    
    cita = Cita()
    cita.nombre_cliente=nombre_Cliente
    cita.rut_cliente=rut_Cliente
    cita.fono_cliente=fono_Cliente
    cita.fecha_cita=fecha
    cita.marca_vehiculo=marca
    cita.modelo_vehiculo=modelo_Vehiculo
    cita.patente_vehiculo=patente.upper()
    cita.estado_cita=None
    cita.agregarCita()




def form_editar_cita():
    # Formulario para edita cita
    print("(Para volver y ver los registros, deje el espacio ID sin responder)")
    id_busq = input("Ingrese la id de la cita a editar \nID: ")
    if  id_busq != "":
        cita = Cita()
        cita.buscarIdCita(id_cita=id_busq)

        print("--- Datos Cliente ---")

        print(f"Nombre cliente: {cita.nombre_cliente}")
        nombre = input("Ingrese nuevo nombre (si no quiere cambiarlo, presione ENTER): ")
        if nombre != "":
            cita.nombre_cliente = nombre

        print(f"RUT cliente: {cita.rut_cliente}")
        rut = input("Ingrese nuevo RUT (si no quiere cambiarlo, presione ENTER): ")
        if rut != "":
            cita.rut_cliente = rut

        print(f"telefono cliente: {cita.fono_cliente}")
        fono = input("Ingrese nuevo telefono (si no quiere cambiarlo, presione ENTER): ")
        if fono != "":
            cita.fono_cliente = fono

        print("--- Datos Cita ---")

        print(f"Fecha cita: {cita.fecha_cita.strftime("%d/%m/%Y")}")
        fecha = input("Ingrese nueva fecha (DD-MM-YYYY) (si no quiere cambiarlo, presione ENTER): ")
        if fecha != "":
            cita.fecha_cita = fecha

        print("--- Datos Vehiculo -- ")

        print(f"Marca vehiculo: {cita.marca_vehiculo}")
        marca = input("Ingrese nueva marca (si no quiere cambiarlo, presione ENTER): ")
        if marca != "":
            cita.marca_vehiculo = marca

        print(f"Modelo vehiculo: {cita.modelo_vehiculo}")
        mod = input("Ingrese nuevo modelo (si no quiere cambiarlo, presione ENTER): ")
        if mod != "":
            cita.modelo_vehiculo = mod

        print(f"Patente vehiculo: {cita.patente_vehiculo}")
        pat = input("Ingrese nueva patente (si no quiere cambiarlo, presione ENTER): ")
        if pat != "":
            cita.patente_vehiculo = pat

        cita.editarCita()
        print("==============================")
        print("Cita actualizada")



def buscar_todos():
    # buscar todos los registros de citas
    cita = Cita()
    lista = cita.buscarTodos()
    if lista:
        for cita in lista:
            print("===========================")
            print(f"id cita: {cita[0]} \n"\
                    f"Cliente: {cita[1]} \n"\
                    f"rut: {cita[2]} \n"\
                    f"teléfono: {cita[3]} \n"\
                    f"Fecha cita: {cita[4].strftime("%d-%m-%Y")} \n"\
                    f"Vehiculo: {cita[5]} \n"\
                    f"Modelo: {cita[6]} \n"\
                    f"Patente: {cita[7]} \n"\
                    f"Estado cita: {cita[8]}")
    else:
        print("No se encontraron registros de citas")