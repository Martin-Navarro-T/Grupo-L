from flask_restful import Resource
from flask import request

CONFIGURACIONES = {
    1:{"nombre":"General"},
    2:{"nombre":"Inicio"},
    3:{"nombre":"Buscar"}
}

class Configuracion(Resource):
    def get(self,id):
        if int(id) in CONFIGURACIONES:
            return CONFIGURACIONES[int(id)] 
        else:
            return "No existe esa configuración", 404 

    def put(self, id): 
        if int(id) in CONFIGURACIONES:
            configuracion = CONFIGURACIONES[int(id)]
            data = request.get_json()
            configuracion.update(data)
            return 201
        else:
            return 'La configuración no existe', 404

    def delete(self,id):
        if int(id) in CONFIGURACIONES:
            del CONFIGURACIONES[int(id)]
            return "La configuración fue eliminada con exito", 204
        else: 
            return "No existe esa configuración", 404
        
class Configuraciones(Resource):
    def get(self):
        return CONFIGURACIONES
    
    def post(self):
        configuracion = request.get_json()
        id = int(max(CONFIGURACIONES.keys()))+1
        CONFIGURACIONES[id] = configuracion
        return CONFIGURACIONES[id], 201