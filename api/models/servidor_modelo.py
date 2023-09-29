from ..database import DatabaseConnection

class Servidor:
    _keys = ["servidor_id", "nombre_servidor", "descripcion"]

    def __init__(self, **kwargs):
        self.servidor_id = kwargs.get("servidor_id")
        self.nombre_servidor = kwargs.get("nombre_servidor")
        self.descripcion = kwargs.get("descripcion")
       
    def serialize (self):
        return {
            "servidor_id": self.servidor_id,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
        }
    
    @classmethod
    def create_servidor(cls, servidor):
        query = """INSERT INTO proyecto_integrador.servidores (nombre_servidor, descripcion)
               VALUES (%(nombre_servidor)s, %(descripcion)s)"""
        params = servidor.__dict__
        DatabaseConnection.execute_query(query, params)

    
    @classmethod
    def delete(cls, servidor):
        query = "DELETE FROM proyecto_integrador.servidores WHERE servidor_id = %(servidor_id)s"
        params = {"servidor_id": servidor.servidor_id}
        DatabaseConnection.execute_query(query, params)

    
    @classmethod
    def get(cls, servidor=None):
        if servidor is not None and servidor.servidor_id is not None:
            query = """SELECT servidor_id, nombre_servidor, descripcion
                       FROM proyecto_integrador.servidores WHERE servidor_id = %(servidor_id)s"""
            params = servidor.__dict__
            result = DatabaseConnection.fetch_one(query, params)
            if result:
                return cls(**dict(zip(cls._keys, result)))
            else:
                return None
        else:
            query = """SELECT servidor_id, nombre_servidor, descripcion
            FROM proyecto_integrador.servidores"""
            results = DatabaseConnection.fetch_all(query)
            servidor = []
            for row in results:
                servidor.append(cls(**dict(zip(cls._keys, row))))
            return servidor

    @classmethod
    def update(cls, servidor_id, updates):
        query = "UPDATE proyecto_integrador.servidores SET "
        servidor_updates = []
        for key, value in updates.items():
            if value is not None:
                servidor_updates.append(f"{key} = %({key})s")
        query += ", ".join(servidor_updates)
        query += " WHERE servidor_id = %(servidor_id)s"

        params = {"servidor_id": servidor_id, **updates}
    
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_usuario(cls, servidor):
        query = """SELECT u.usuario_id, u.nombre_usuario, u.contraseña, u.email, u.foto_img
                    FROM proyecto_integrador.usuarios u
                   INNER JOIN proyecto_integrador.servidores_onboarding so ON u.usuario_id = u.usuario_id
                   WHERE so.servidor_id = %(servidor_id)s"""
        params = servidor.__dict__
        results = DatabaseConnection.fetch_all(query, params)
        users = []

        for row in results:
            users.append(dict(zip(Servidor._keys, row)))
        return users

    @classmethod
    def registro(cls, usuario, servidor):
        query = """INSERT INTO proyecto_integrador.servidores_onboarding (usuario_id, servidor_id)
                   VALUES (%(usuario_id)s, %(servidor_id)s)"""
        params = {"usuario_id": usuario.usuario_id, "server_id": servidor.servidor_id}
        DatabaseConnection.execute_query(query, params)
