from .conexion import ConexionBD


class Cita:

    id_cita:int
    nombre_cliente:str
    rut_cliente:str
    fono_cliente:str
    fecha_cita:str
    marca_vehiculo:str
    modelo_vehiculo:str
    patente_vehiculo:str
    estado_cita:str

    def agregarCita(self):
        c = ConexionBD()
        sql = """
            INSERT INTO CITAS(nombre_cliente,rut_cliente,fono_cliente,fecha_cita,marca_vehiculo,modelo_vehiculo,patente_vehiculo)
            VALUES(:nom,:rut,:fono,:fecha,:marca,:model,:pat)
            """
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
            FROM CITAS WHERE rut_cliente = :rut"""
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

    def buscarIdCita(self, id_cita):
        c = ConexionBD()
        sql = """
            SELECT id_cita, nombre_cliente, rut_cliente, fono_cliente, fecha_cita, marca_vehiculo, modelo_vehiculo, patente_vehiculo, estado_cita
            FROM CITAS WHERE id_cita = :ic
            """
        c.cursor.execute(sql, ic=id_cita)
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

    def buscarTodos(self):
        c = ConexionBD()
        sql = """
            SELECT id_cita, nombre_cliente, rut_cliente, fono_cliente, fecha_cita, marca_vehiculo, modelo_vehiculo, patente_vehiculo, estado_cita 
            FROM CITAS"""
        c.cursor.execute(sql)

        return c.cursor.fetchall() #lista de tuplas

    def editarCita(self):
        c = ConexionBD()
        sql = """
            UPDATE citas
            SET nombre_cliente = :nom,
                rut_cliente = :rut,
                fono_cliente = :fono,
                fecha_cita = :fecha,
                marca_vehiculo = :marca,
                modelo_vehiculo = :modelo,
                patente_vehiculo = :pat
            WHERE id_cita = :id
                """
        c.cursor.execute(sql,
                         id = self.id_cita,
                         nom = self.nombre_cliente,
                         rut = self.rut_cliente,
                         fono = self.fono_cliente,
                         fecha = self.fecha_cita,
                         marca = self.marca_vehiculo,
                         modelo = self.modelo_vehiculo,
                         pat = self.patente_vehiculo)
        c.conexion.commit()
    