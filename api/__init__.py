from flask import Flask, render_template, request
from flask_cors import CORS
from config import Config
from.routes.bp_usuario import bp_usuarios
from.routes.bp_canal import bp_canales
from.routes.bp_servidor import bp_servidor
from.routes.bp_mensaje import bp_mensajes
from.database import DatabaseConnection

def init_app():
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

    CORS(app, supports_credentials=True)
    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(bp_usuarios, url_prefix="/usuarios")
    app.register_blueprint(bp_canales, url_prefix="/canales")
    app.register_blueprint(bp_servidor, url_prefix="/servidor")
    app.register_blueprint(bp_mensajes, url_prefix="/mensaje")
    
    return app





    