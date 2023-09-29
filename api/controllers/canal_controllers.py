from ..models.canal_modelo import Canales
from flask import request
from flask import jsonify

class CanalesController:

    @classmethod
    def create_canal(cls):
        data = request.json
        nuevo_canal = Canales(
            servidor_id=data.get("servidor_id"),
            nombre_canal=data.get("nombre_canal"),
        )
        Canales.create_canal(nuevo_canal)  
        return {'message': "Canal creado con éxito"}, 200


    @classmethod
    def get_canal_id(self, canal_id):
        canal = Canales(canal_id=canal_id)
        canal = Canales.get_canal_id(canal)
        if canal:
            return canal.serialize(), 200

    @classmethod
    def get_canales(cls):
        canales = Canales.get_all()
        canales_data = [
            {
                "canal_id": canal.canal_id,
                "nombre_canal": canal.nombre_canal
            }
            for canal in canales
        ]
        return jsonify(canales_data), 200

    @classmethod
    def update_canales(cls, canal_id):
        data = request.json
        canal = Canales(
            canal_id=canal_id,
            nombre_canal=data.get("nombre_canal"),
            servidor_id=data.get("servidor_id"),
        )
        Canales.update(canal)
        return {"message": "Canal actualizado exitosamente"}, 200

    @classmethod
    def delete_canal(self, canal_id):
        canal = Canales(canal_id=canal_id)
        Canales.delete(canal)
        return {'message': "Canal eliminado con éxito"}, 200
       
    @classmethod
    def delete_canales(self):
        Canales.delete_all()
        return {'message': "Todos los canales han sido eliminados"}, 200
