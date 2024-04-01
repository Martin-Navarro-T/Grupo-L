from flask_restful import Resource
from flask import request

NOTIFICACIONES = {
    1:{"usuario":"Ian Olmedo", "mensaje":"Mañana es tu fecha de vencimiento", "hora":"27/04/2024"},
    2:{"usuario":"Reynier Lopez", "mensaje":"Mañana es tu fecha de vencimiento", "hora":"29/04/2024"},
}

CONFIGURACIONES = {
    1:{"nombre":"General"},
    2:{"nombre":"Inicio"},
    3:{"nombre":"Buscar"}
}

VALORACIONES = {
    1:{"cliente":"Martin Navarro", "libro":"Harry Potter", "fecha":"27/04/2024", "mensaje":"5 estrellas"},
    2:{"cliente":"Zoe Choque", "libro":"Nacidos de la bruma", "fecha":"28/04/2024", "mensaje":"2 estrellas"},
}
COMENTARIOS = {
    1:{"cliente":"Nahuel Vicente", "libro":"Programación para tontos", "fecha":"27/04/2024", "mensaje":"Muy bueno"},
    2:{"cliente":"Olivia Rubio", "libro":"Redes de Datos III", "fecha":"28/04/2024", "mensaje":"Muy malo"},
}
class Notificaciones(Resource):
    #def post(self):
    #    notificacion = request.get_json()
    #    id = int(max(NOTIFICACIONES.keys()))+1
    #    NOTIFICACIONES[id] = notificacion 
    #    return NOTIFICACIONES[id], "El mensaje fue enviado correctamente", 201

    def post(self):
        notificacion = request.get_json()
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[id] = notificacion
        return NOTIFICACIONES[id], 201

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
    
class Valoracion(Resource):
    def get(self):
        return VALORACIONES
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(VALORACIONES.keys()))+1
        VALORACIONES[id] = prestamo
        return VALORACIONES[id], 201

class Comentarios(Resource):
    def get(self):
        return COMENTARIOS
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(COMENTARIOS.keys()))+1
        COMENTARIOS[id] = prestamo
        return COMENTARIOS[id], 201
    


