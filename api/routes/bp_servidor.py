from flask import Blueprint
from ..controllers.servidor_controllers import ServidorController

bp_servidor = Blueprint ("bp_servidor", __name__)

bp_servidor.route("/", methods=["GET"])(ServidorController.get_servidores)
bp_servidor.route("/<servidor_id>", methods=["GET"])(ServidorController.get_servidor)
bp_servidor.route("/", methods=["POST"])(ServidorController.create_servidor)
bp_servidor.route("/<servidor_id>", methods=["PUT"])(ServidorController.update_servidor)
bp_servidor.route("/<servidor_id>", methods=["DELETE"])(ServidorController.delete_servidor)
