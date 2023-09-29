from flask import Blueprint
from ..controllers.mensaje_controllers import MensajesController

bp_mensajes = Blueprint ("bp_mensajes", __name__)

bp_mensajes.route("/", methods=["GET"])(MensajesController.get)
bp_mensajes.route("/<usuario_id>", methods=["GET"])(MensajesController.get_mensajes_id)
bp_mensajes.route("/", methods=["POST"])(MensajesController.create_mensaje)
bp_mensajes.route("/<usuario_id>", methods=["PUT"])(MensajesController.update_mensajes)
bp_mensajes.route("/<usuario_id>", methods=["DELETE"])(MensajesController.delete_mensaje)
bp_mensajes.route("/<usuario_id>/servers", methods=["GET"])(MensajesController.get)