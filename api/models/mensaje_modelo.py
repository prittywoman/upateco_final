from ..database import DatabaseConnection

class Mensajes:
    _keys = ["mensaje_id", "usuario_id", "canal_id", "contenido", "fecha_creacion"]

    def __init__(self, **kwargs):
        self.mensaje_id = kwargs.get("mensaje_id")
        self.usuario_id = kwargs.get("usuario_id")
        self.canal_id = kwargs.get("canal_id")
        self.contenido = kwargs.get("contenido")
        self.fecha_creacion = kwargs.get("fecha_creacion")

    def serialize (self):
        return {
            "mensaje_id": self.mensaje_id,
            "usuario_id": self.usuario_id,
            "canal_id": self.canal_id,
            "contenido": self.contenido,
            "fecha_creacion": self.fecha_creacion,
        }
    
    @classmethod
    def create(cls, mensajes):
        query= """INSERT INTO proyecto_integrador.mensajes (usuario_id, canal_id, contenido, fecha_creacion)
            VALUES (%(usuario_id)s, %(canal_id)s, %(contenido)s, %(fecha_creacion)s )"""
        params = mensajes.__dict__
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def delete(cls, mensajes):
        query= "DELETE FROM proyecto_integrador.mensajes WHERE mensaje_id = %(mensaje_id)s"
        params = mensajes.__dict__
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def get(cls, mensajes=None):
            query= """SELECT mensaje_id, usuario_id, canal_id, contenido, fecha_creacion
                    FROM proyecto_integrador.mensajes"""
            result = DatabaseConnection.fetch_all(query)
            mensajes = []
            for row in result:
                mensajes.append(cls(**dict(zip(cls._keys, row))))
            return mensajes
    
    @classmethod
    def update(cls, mensaje):
        query = "UPDATE proyecto_integrador.mensajes SET "
        mensaje_data = mensaje.__dict__
        mensaje_updates = []
        for key in mensaje_data.keys():
            if mensaje_data[key] is not None and key not in [
                "mensaje_id",
                "fecha_creacion",
            ]:
                mensaje_updates.append(f"{key} = %({key})s")
        query += ", ".join(mensaje_updates)
        query += ", fecha_creacion = CURRENT_TIMESTAMP WHERE mensaje_id = %(mensaje_id)s"
        DatabaseConnection.execute_query(query, mensaje_data)

    @classmethod
    def get_mensaje_id(cls, mensaje):
        query = """SELECT mensaje_id, usuario_id, canal_id, contenido, fecha_creacion FROM proyecto_integrador.mensajes WHERE mensaje_id = %(mensaje_id)s;"""
        params = mensaje.__dict__
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None

    @classmethod
    def get_mensaje_canal(cls, mensaje):
        query = """SELECT mensaje_id, usuario_id, canal_id, contenido, fecha_creacion
                FROM proyecto_integrador.mensajes WHERE canal_id = %(canal_id)s ORDER BY fecha_creacion ASC"""
        params = mensaje.__dict__
        results = DatabaseConnection.fetch_all(query, params)
        mensaje= []
        for row in results:
            mensaje.append(cls(**dict(zip(cls._keys, row))))
        return mensaje

    @classmethod
    def get_messages_usuario(cls, mensaje):
        query = """SELECT mensaje_id, usuario_id, canal_id, contenido, fecha_creacion
                FROM proyecto_integrador.mensajes WHERE usuario_id = %(usuario_id)s"""
        params = mensaje.__dict__
        results = DatabaseConnection.fetch_all(query, params)
        mensaje = []
        for row in results:
            mensaje.append(cls(**dict(zip(cls._keys, row))))
        return mensaje
