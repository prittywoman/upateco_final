from ..database import DatabaseConnection

class Canales():
    _keys = ["canal_id", "servidor_id", "nombre_canal"]

    def __init__(self, **kwargs):
        self.canal_id = kwargs.get("canal_id")
        self.servidor_id = kwargs.get("servidor_id")
        self.nombre_canal = kwargs.get("nombre_canal")

    def serialize (self):
        return {
            "canal_id": self.canal_id,
            "servidor_id": self.servidor_id,
            "nombre_canal": self.nombre_canal,
        }
    
    @classmethod
    def create_canal(cls, canales):
        query = """INSERT INTO proyecto_integrador.canales (servidor_id, nombre_canal)
                   VALUES (%(servidor_id)s, %(nombre_canal)s)"""
        params = {
            'servidor_id': canales.servidor_id,
            'nombre_canal': canales.nombre_canal,
        }
        DatabaseConnection.execute_query(query, params)

    
    @classmethod
    def delete(cls, canales):
        query= "DELETE FROM proyecto_integrador.canales WHERE canal_id = %(canal_id)s"
        params = canales.__dict__
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def get_all(cls):
        query = "SELECT canal_id, servidor_id, nombre_canal FROM proyecto_integrador.canales"
        results = DatabaseConnection.fetch_all(query)
        canales = []
        for row in results:
            canales.append(cls(**dict(zip(cls._keys, row))))
        return canales

    @classmethod
    def update(cls, canal):
        query = "UPDATE proyecto_integrador.canales SET "
        canal_data = canal.__dict__
        canal_updates = []
        for key in canal_data.keys():
            if canal_data[key] is not None and key != "canal_id":
                canal_updates.append(f"{key} = %({key})s")
        query += ", ".join(canal_updates)
        query += " WHERE canal_id = %(canal_id)s;"
        DatabaseConnection.execute_query(query, canal_data)

    @classmethod
    def get_canal_id(cls, canal):
        query = """SELECT canal_id, servidor_id, nombre_canal
                FROM proyecto_integrador.canales WHERE canal_id = %(canal_id)s"""
        params = canal.__dict__
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None

    @classmethod
    def get_channels_servidor(cls, canal):
        query = """SELECT canal_id, servidor_id, nombre_canal
                FROM proyecto_integrador.canales WHERE servidor_id = %(servidor_id)s"""
        params = canal.__dict__
        results = DatabaseConnection.fetch_all(query, params)
        canal = []
        for row in results:
            canal.append(cls(**dict(zip(cls._keys, row))))
        return canal

