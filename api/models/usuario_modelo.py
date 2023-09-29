from ..database import DatabaseConnection

class Usuario:
    _keys = ["usuario_id", "nombre_usuario", "contraseña", "email", "foto_img"]

    def __init__(self, **kwargs):
        self.usuario_id = kwargs.get("usuario_id")
        self.nombre_usuario = kwargs.get("nombre_usuario")
        self.contraseña = kwargs.get("contraseña")
        self.email = kwargs.get("email")
        self.foto_img = kwargs.get("foto_img")

    def serialize (self):
        return {
            "usuario_id": self.usuario_id,
            "nombre_usuario": self.nombre_usuario,
            "contraseña": self.contraseña,
            "email": self.email,
            "foto_img": self.foto_img,
        }
    
    @classmethod
    def create(cls, usuario):
        query= """INSERT INTO proyecto_integrador.usuarios (nombre_usuario, contraseña, email, foto_img)
            VALUES (%(nombre_usuario)s, %(contraseña)s, %(email)s, %(foto_img)s)"""
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def delete(cls, usuario):
        query= "DELETE FROM proyecto_integrador.usuarios WHERE usuario_id = %(usuario_id)s"
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def get_usuario(cls, usuario_id):
        query = """SELECT usuario_id, nombre_usuario, contraseña, email, foto_img
               FROM proyecto_integrador.usuarios
               WHERE usuario_id = %(usuario_id)s"""
    
        params = {"usuario_id": usuario_id}
        result = DatabaseConnection.fetch_one(query, params)
    
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None  

    @classmethod
    def get_all(cls):
        query = "SELECT usuario_id, nombre_usuario, contraseña, email, foto_img FROM proyecto_integrador.usuarios"
        results = DatabaseConnection.fetch_all(query)
        usuarios = []

        for row in results:
            usuario = cls(
                usuario_id=row[0],
                nombre_usuario=row[1],
                contraseña=row[2],
                email=row[3],
                foto_img=row[4]
            )
            usuarios.append(usuario)

        return usuarios

    @classmethod
    def update(cls, usuario):
        query = "UPDATE proyecto_integrador.usuarios SET "
        usuario_data = usuario.__dict__
        usuario_updates = []
        for key in usuario_data.keys():
            if usuario_data[key] is not None and key != "usuario_id":
                usuario_updates.append(f"{key} = %({key})s")
        query += ", ".join(usuario_updates)
        query += " WHERE usuario_id = %(usuario_id)s"
        DatabaseConnection.execute_query(query, usuario_data)

    @classmethod
    def login(cls, usuario):
        query = """SELECT usuario_id, nombre_usuario, contraseña, email, foto_img
                    FROM proyecto_integrador.usuarios
                    WHERE nombre_usuario = %(nombre_usuario)s AND contraseña = %(contraseña)s"""
        params = usuario.__dict__
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None
