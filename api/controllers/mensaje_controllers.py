from ..models.mensaje_modelo import Mensajes  
from flask import request

class MensajesController:
    @classmethod
    def create_mensaje(cls):
        data = request.json
        mensaje = Mensajes(
            usuario_id=data.get("usuario_id"),
            canal_id=data.get("canal_id", ""),
            contenido=data.get("contenido"),
            fecha_creacion=data.get("fecha_creacion"),
        )
        Mensajes.create_mensaje()  
        return {'message': "Mensaje creado con éxito"}, 200

    @classmethod
    def get_mensajes_id(cls, mensaje_id):
        mensaje = Mensajes(mensaje_id=mensaje_id)  
        mensaje = Mensajes.get_mensajes_id(mensaje)
        if mensaje:
            return mensaje.serialize(), 200
   
    @classmethod
    def get(cls):
        mensaje = []
        mensaje = mensaje(
            canal_id=request.args.get("canal_id"),
            usuario_id=request.args.get("usuario_id"),
        )
        if mensaje.canal_id:
            for mensaje in Mensajes.get_mensaje_canal(mensaje):
                mensaje.append(mensaje.serialize())
        elif mensaje.usuario_id:
            for mensaje in Mensajes.get_mensaje_usuario(mensaje):
                mensaje.append(mensaje.serialize())
        else:
            for mensaje in Mensajes.get():
                mensaje.append(mensaje.serialize())

        return mensaje, 200

    @classmethod
    def update_mensajes(cls, mensaje_id):
        data = request.json
        
        mensaje = Mensajes( 
            id = mensaje_id, 
            canal_id = data.get("canal_id"),
            contenido = data.get("contenido"),
            usuario_id = data.get("usuario_id")
        )
        mensaje.update(mensaje)  
        return {'message': "Mensaje actualizado con éxito"}, 200
        
    @classmethod
    def delete_mensaje(cls, mensaje_id):
        mensaje = Mensajes(mensaje_id=mensaje_id)  
        Mensajes.delete(mensaje) 
        return {'mensaje': "Mensaje eliminado con éxito"}, 200
       
    @classmethod
    def delete_mensajes(cls):
        Mensajes.delete_all()  
        return {'message': "Todos los mensajes han sido eliminados"}, 200
