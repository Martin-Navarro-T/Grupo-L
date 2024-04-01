from flask_restful import Resource
from flask import request

VALORACIONES = {
    1:{"cliente":"Martin Navarro", "libro":"Harry Potter", "fecha":"27/04/2024", "mensaje":"5 estrellas"},
    2:{"cliente":"Zoe Choque", "libro":"Nacidos de la bruma", "fecha":"28/04/2024", "mensaje":"2 estrellas"},
}

class Valoracion(Resource):
    def get(self):
        return VALORACIONES
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(VALORACIONES.keys()))+1
        VALORACIONES[id] = prestamo
        return VALORACIONES[id], 201