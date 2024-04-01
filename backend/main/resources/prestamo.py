from flask_restful import Resource
from flask import request

PRESTAMOS = {
    1:{"cliente":"Martin Navarro", "libro":"Harry Potter", "vencimiento":"27/04/2024", "devuelto":"no"},
    2:{"cliente":"Zoe Choque", "libro":"Nacidos de la bruma", "vencimiento":"28/04/2024", "devuelto":"no"},
}
   
#post crea y put actualiza
class Prestamo(Resource):
    def get(self,id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)]
        else:
            return 'El prestamo no existe', 404
    
    def delete(self, id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS[(int(id))]
            return "El prestamo fue eliminado", 204
        else:
            return 'El prestamo no existe', 404

    def put(self, id):
        if int(id) in PRESTAMOS:
            prestamo = PRESTAMOS[int(id)]
            data = request.get_json()
            prestamo.update(data)
            return "El prestamo fue actualizado", 201
        else:
            return 'El prestamo no existe', 404

class Prestamos(Resource):
    def get(self):
        return PRESTAMOS
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(PRESTAMOS.keys()))+1
        PRESTAMOS[id] = prestamo
        return PRESTAMOS[id],  201
    
    
    