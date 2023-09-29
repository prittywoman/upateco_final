from flask import Blueprint
from ..controllers.usuario_controllers import UsuarioController

bp_usuarios = Blueprint ("bp_usuarios", __name__)

bp_usuarios.route("/", methods=["GET"])(UsuarioController.get_usuarios)
bp_usuarios.route("/<usuario_id>", methods=["GET"])(UsuarioController.get_usuario)
bp_usuarios.route("/", methods=["POST"])(UsuarioController.create_usuario)
bp_usuarios.route("/<usuario_id>", methods=["PUT"])(UsuarioController.update_usuario)
bp_usuarios.route("/<usuario_id>", methods=["DELETE"])(UsuarioController.delete_usuario)
bp_usuarios.route("/login", methods=["POST"])(UsuarioController.login)
