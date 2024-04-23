from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import os
from flask_sqlalchemy import SQLAlchemy

api = Api()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    load_dotenv()

    if not os.path.exists(os.getenv('DATABASE_PATH')+ os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME'))
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.getenv('DATABASE_PATH') + os.getenv('DATABASE_NAME')
    db.init_app(app)

    import main.resources as resources

    api.add_resource(resources.UsuariosResources, "/Usuarios")
    api.add_resource(resources.UsuarioResources, "/Usuario/<id>")
    #api.add_resource(resources.Sign_inResources,"/Sign_in")
    #api.add_resource(resources.LoginResources,"/Login")
    api.add_resource(resources.LibrosResources,"/Libros")
    api.add_resource(resources.LibroResources,"/Libro/<id>")
    api.add_resource(resources.PrestamosResources, "/Prestamos")
    api.add_resource(resources.PrestamoResources, "/Prestamo/<id>")   
    api.add_resource(resources.NotificacionesResources, "/Notificaciones")
    api.add_resource(resources.ValoracionResources, "/Valoracion")
    api.add_resource(resources.ConfiguracionResources, "/Configuracion/<id>")
    api.add_resource(resources.ConfiguracionesResources, "/Configuraciones")
    api.add_resource(resources.AutorResources, "/Autor/<id>")
    api.add_resource(resources.AutoresResources, "/Autores")
    
    api.init_app(app)
    
    return app 
