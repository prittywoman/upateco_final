from ..models.servidor_modelo import Servidor
from flask import request

class ServidorController:
    @classmethod
    def create_servidor(cls):
        data = request.json
        servidor = Servidor(
            nombre_servidor=data.get("nombre_servidor"),
            descripcion=data.get("descripcion"),
        )
        Servidor.create_servidor(servidor) 
        return {'message': "Servidor creado con éxito"}, 200


    @classmethod
    def get_servidor(cls, servidor_id):
        
        servidor = Servidor(servidor_id=servidor_id)
        servidor = Servidor.get(servidor)
        if servidor:
            return {
                "servidor_id": servidor.servidor_id,
                "nombre_servidor": servidor.nombre_servidor,
                "descripcion": servidor.descripcion
            }, 200
        else:
            return {'message': "Servidor no encontrado"}, 404

    @classmethod
    def get_servidores(cls):
        servidores = Servidor.get()
        servidores_data = [{
            "servidor_id": servidor.servidor_id,
            "nombre_servidor": servidor.nombre_servidor,
            "descripcion": servidor.descripcion
        } for servidor in servidores]
        return {"servidores": servidores_data}, 200


    @classmethod
    def update_servidor(cls, servidor_id):
        data = request.json
        servidor_updates = {
            "nombre_servidor": data.get("nombre_servidor"),
            "descripcion": data.get("descripcion"),
        }
    
        Servidor.update(servidor_id, servidor_updates)
    
        return {'message': "Servidor actualizado con éxito"}, 200

    @classmethod
    def delete_servidor(cls, servidor_id):
        servidor = Servidor.get(servidor_id)
    
        if servidor:
            Servidor.delete(servidor)
            return {'message': "Servidor eliminado con éxito"}, 200
        else:
            return {'message': "Servidor no encontrado"}, 404

    @classmethod
    def get_usuario(cls, servidor_id):
        servidor = Servidor(servidor_id=servidor_id)
        usuarios = []
        for user in Servidor.get_usuario(servidor):
            usuarios.append(usuarios.serialize())
        return usuarios, 200

    @classmethod
    def registro_usuario(cls, servidor_id):
        data = request.json
        servidor = Servidor(servidor_id=servidor_id)
        from ..models.usuario_modelo import Usuario

        usuario = Usuario(usuario_id=data.get("usuario_id"))
        Servidor.registro(usuario, servidor)
        return {"message": "Usuario registrado con exito"}, 200
