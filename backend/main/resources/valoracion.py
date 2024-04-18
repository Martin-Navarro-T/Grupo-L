from flask_restful import Resource
from flask import request,jsonify
from .. import db
from main.models import ValoracionesModel


class Valoracion(Resource):
    def get(self):
        valoraciones = db.session.query(ValoracionesModel).all()
        return jsonify([valoracion.to_json() for valoracion in valoraciones])
    
    def post(self):
        valoracion = ValoracionesModel.from_json(request.get_json())
        db.session.add(valoracion)
        db.session.commit
        return valoracion.to_json(), 201