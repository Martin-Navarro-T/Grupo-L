from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ConfiguracionModel



class Configuracion(Resource):
    def get(self,id):
        configuracion = db.session.query(ConfiguracionModel).get_or_404(id)
        return configuracion.to_json(), 201


    def put(self, id): 
        configuracion = db.session.query(ConfiguracionModel).get_or_404(id)
        data = request.get_json().items()
        for key, values in data:
            setattr(configuracion, key, values)
        db.session.add(configuracion)
        db.session.commit() 
        return configuracion.to_json(), 201


    def delete(self,id):
        configuracion = db.session.query(ConfiguracionModel).get_or_404(id)
        db.session.delete(configuracion)
        db.session.commit()
        return 'Ha sido eliminado correctamente', 204
        
class Configuraciones(Resource):
    def get(self):
        configuraciones = db.session.query(ConfiguracionModel).all()
        return jsonify([configuracion.to_json() for configuracion in configuraciones])
    
    def post(self):
        configuracion = ConfiguracionModel.from_json(request.get_json())
        db.session.add(configuracion)
        db.session.commit()
        return configuracion.to_json(), 201