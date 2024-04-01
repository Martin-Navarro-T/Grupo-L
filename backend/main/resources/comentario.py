from flask_restful import Resource
from flask import request

COMENTARIOS = {
    1:{"cliente":"Nahuel Vicente", "libro":"Programación para tontos", "fecha":"27/04/2024", "mensaje":"Muy bueno"},
    2:{"cliente":"Olivia Rubio", "libro":"Redes de Datos III", "fecha":"28/04/2024", "mensaje":"Muy malo"},
}

class Comentarios(Resource):
    def get(self):
        return COMENTARIOS
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(COMENTARIOS.keys()))+1
        COMENTARIOS[id] = prestamo
        return COMENTARIOS[id], 201