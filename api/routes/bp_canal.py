from flask import Blueprint
from ..controllers.canal_controllers import CanalesController

bp_canales = Blueprint ("bp_canales", __name__)

bp_canales.route("/", methods=["GET"])(CanalesController.get_canales)
bp_canales.route("/<canal_id>", methods=["GET"])(CanalesController.get_canal_id)
bp_canales.route("/", methods=["POST"])(CanalesController.create_canal)
bp_canales.route("/<canal_id>", methods=["PUT"])(CanalesController.update_canales)
bp_canales.route("/<canal_id>", methods=["DELETE"])(CanalesController.delete_canal)
