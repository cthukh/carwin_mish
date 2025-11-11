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
    rut_Cliente=input("Ingrese Rut: ")

    while verifRut(rut_Cliente) == False :
        print("RUT no valido, vuelva a ingresar")
        rut_Cliente=input("Ingrese Rut: ")

    fono_Cliente=input("Número De telefono: ")

    # vehiculo
    print("\n===== Datos Del Vehiculo ====")
    marca=input("Marca Del Vehiculo: ")
    # modelo_vehiculo=input(f"¿ Cual es el modelo del vehículo ?: ")
    modelo_Vehiculo=input("Modelo del vehículo: ")
    patente=input("Patente del vehículo: ")

    # fecha
    print("\nFecha De Agendacion De cita")
    fecha=input("¿Cúando desea agendar su lavado de Vehiculo ?: ")
    fecha_Cita = fecha.strip().replace("/","-")

    print(f"Se ha Agendado una cita para: {nombre_Cliente} del vehiculo {marca} Modelo {modelo_Vehiculo}. Para el dia {fecha_Cita}")
    
    cita = Cita(nombre_cliente=nombre_Cliente,
                rut_cliente=rut_Cliente,
                fono_cliente=fono_Cliente,
                fecha_cita=fecha,
                marca_vehiculo=marca,
                modelo_vehiculo=modelo_Vehiculo,
                patente_vehiculo=patente,
                estado_cita=None)
    cita.agregarCita()




def editar_cita():
    # Formulario para edita cita
    rut_busq = input("Ingrese rut para buscar a la persona \nRUT >>> ")
    cita = Cita()

    while verifRut(rut_busq) == False :
        print("RUT no valido, vuelva a ingresar")
        rut_busq=input("Ingrese RUT >>> ")

    cita.buscarRut(rut_cliente=rut_busq)
    # print(cita.nombre_cliente)


