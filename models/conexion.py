import oracledb

class ConexionBD:
    def __init__(self):
        self.conexion = oracledb.connect(
            user="AYAME",
            password="inacap",
            dsn="localhost/XE",
        )
        self.cursor = self.conexion.cursor()