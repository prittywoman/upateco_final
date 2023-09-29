from ..models.usuario_modelo import Usuario
from flask import request, session

class UsuarioController:
    @classmethod
    def create_usuario(cls):
        data = request.json
        usuario = Usuario(
            nombre_usuario=data.get("nombre_usuario"),
            contraseña=data.get("contraseña"),
            email=data.get("email"),
            foto_img=data.get("foto_img"),
        )
        Usuario.create(usuario)
        return {'message': "Usuario creado con éxito"}, 200

    @classmethod
    def get_usuario(self, usuario_id):
        usuario = Usuario.get_usuario(usuario_id)
        if usuario:
            return {
                'usuario_id': usuario.usuario_id,
                'nombre_usuario': usuario.nombre_usuario,
                'contraseña': usuario.contraseña,
                'email': usuario.email,
                'foto_img': usuario.foto_img
            }, 200
        else:
           
            return {'message': "Usuario no encontrado"}, 404

    @classmethod
    def get_usuarios(self):
        usuarios = Usuario.get_all()
        usuarios_data = [{
            'usuario_id': usuario.usuario_id,
            'nombre_usuario': usuario.nombre_usuario,
            'contraseña': usuario.contraseña,
            'email': usuario.email,
            'foto_img': usuario.foto_img
        } for usuario in usuarios]
        return {'usuarios': usuarios_data}, 200

    @classmethod
    def update_usuario(cls, usuario_id):
        data = request.json
        usuario = Usuario(
       
            usuario_id=usuario_id,
            nombre_usuario=data.get("nombre_usuario"),
            contraseña=data.get("contraseña"),
            email=data.get("email"),
            foto_img=data.get("foto_img"),
        )
        Usuario.update(usuario)
        return {'message': "Usuario actualizado con éxito"}, 200
        
    @classmethod
    def delete_usuario(cls, usuario_id):
        usuario = Usuario(usuario_id=usuario_id)
        Usuario.delete(usuario)
        return {'message': "Usuario eliminado con éxito"}, 200
        
    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(
            nombre_usuario=data.get("nombre_usuario"),
            contraseña=data.get("contraseña"),
        )
        print(usuario.serialize())
        usuario = Usuario.login(usuario)
        if usuario:
            session["usuario_id"] = usuario.usuario_id
            session["nombre_usuario"] = usuario.nombre_usuario
            session["email"] = usuario.email
            session["foto_img"] = usuario.foto_img
            return usuario.serialize(), 200
        return {"message": "Credencial invalida"}, 401
    

    
