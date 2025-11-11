from .conexion import ConexionBD


class Cita:
    def __init__(self,
                 nombre_cliente:str,
                 rut_cliente:str,
                 fono_cliente:str,
                 fecha_cita:str,
                 marca_vehiculo:str,
                 modelo_vehiculo:str,
                 patente_vehiculo:str,
                 estado_cita:str):
        self.nombre_cliente   = nombre_cliente
        self.rut_cliente      = rut_cliente
        self.fono_cliente     = fono_cliente
        self.fecha_cita       = fecha_cita
        self.marca_vehiculo   = marca_vehiculo
        self.modelo_vehiculo  = modelo_vehiculo
        self.patente_vehiculo = patente_vehiculo
        self.estado_cita      = estado_cita

    def agregarCita(self):
        c = ConexionBD()
        sql = """INSERT INTO CITAS(nombre_cliente,rut_cliente,fono_cliente,fecha_cita,marca_vehiculo,modelo_vehiculo,patente_vehiculo)
        VALUES(:nom,:rut,:fono,:fecha,:marca,:model,:pat)"""
        c.cursor.execute(sql,
                         nom   = self.nombre_cliente,
                         rut   = self.rut_cliente,
                         fono  = self.fono_cliente,
                         fecha = self.fecha_cita,
                         marca = self.marca_vehiculo,
                         model = self.modelo_vehiculo,
                         pat   = self.patente_vehiculo)
        c.conexion.commit()

    def buscarRut(self,rut_cliente):
        c = ConexionBD()
        sql= """
            SELECT id_cita, nombre_cliente, rut_cliente, fono_cliente, fecha_cita, marca_vehiculo, modelo_vehiculo, patente_vehiculo, estado_cita
            FROM CITAS WHERE rut_cliente = :rut """
        c.cursor.execute(sql, rut=rut_cliente)
        fila = c.cursor.fetchone()
        self.id_cita = fila[0]
        self.nombre_cliente = fila[1]
        self.rut_cliente = fila[2]
        self.fono_cliente = fila[3]
        self.fecha_cita = fila[4]
        self.marca_vehiculo = fila[5]
        self.modelo_vehiculo = fila[6]
        self.patente_vehiculo = fila[7]
        self.estado_cita = fila[8]

    def editarCita(self):
        c = ConexionBD()
        sql = """
            
                """
        c.cursor.execute(sql)
        c.conexion.commit()
    