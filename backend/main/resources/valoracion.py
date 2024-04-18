from flask_restful import Resource
from flask import request,jsonify
from .. import db
from main.models import ValoracionesModel

VALORACIONES = {
    1:{"cliente":"Martin Navarro", "libro":"Harry Potter", "fecha":"27/04/2024", "mensaje":"5 estrellas"},
    2:{"cliente":"Zoe Choque", "libro":"Nacidos de la bruma", "fecha":"28/04/2024", "mensaje":"2 estrellas"},
}

class Valoracion(Resource):
    def get(self):
        valoraciones = db.session.query(ValoracionesModel).all()
        return jsonify([valoracion.to_json() for valoracion in valoraciones])
    
    def post(self):
        valoracion = ValoracionesModel.from_json(request.get_json())
        db.session.add(valoracion)
        db.session.commit
        return valoracion.to_json(), 201