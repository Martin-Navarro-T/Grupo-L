from flask_restful import Resource
from flask import request
from .. import db
from main.models import UsuarioModel

class Sign_in(Resource):
    def post(self):
        cuenta = UsuarioModel.from_json(request.get_json())
        db.session.add(cuenta)
        db.session.commit
        return cuenta.to_json(), 201

class Login(Resource):
    def post(self):
        cuenta = UsuarioModel.from_json(request.get_json())
        db.session.add(cuenta)
        db.session.commit
        return cuenta.to_json(), 201

