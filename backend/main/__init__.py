from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

api = Api()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    api.add_resource(resources.UsuariosResources, "/Usuarios")
    api.add_resource(resources.UsuarioResources, "/Usuario/<id>")
    api.add_resource(resources.sign_inResources,"/sing_in/<id>")
    api.add_resource(resources.LoginResources,"/login/<id>")
    api.add_resource(resources.LibrosResources,"/Libros")
    api.add_resource(resources.LibrosResources,"/Libro/<id>")
    api.add_resource(resources.PrestamosResources, "/Prestamos")
    api.add_resource(resources.PrestamoResources, "/Prestamo/<id>")   
    api.add_resource(resources.NotificacionesResources, "/Notificaciones")
    api.add_resource(resources.ComentariosResources, "/Comentarios")
    api.add_resource(resources.ValoracionResources, "/Valoracion")
    api.add_resource(resources.ConfiguracionResources, "/Configuracion")
    api.init_app(app)
    
    return app 