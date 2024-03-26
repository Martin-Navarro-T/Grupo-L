from flask_restful import Resource
from flask import request

NOTIFICACIONES = {
    1:{"usuario":"Nahuel Vicente", "mensaje":"Mañana es tu fecha de vencimiento", "hora":"27/04/2024"},
    2:{"usuario":"Olivia Rubio", "mensaje":"Mañana es tu fecha de vencimiento", "hora":"29/04/2024"},
}

CONFIGURACIONES = {
    1:{"nombre":"General"},
    2:{"nombre":"Inicio"},
    3:{"nombre":"Buscar"}
}

VALORACIONES = {
    1:{"cliente":"Nahuel Vicente", "libro":"Harry Potter", "fecha":"27/04/2024", "mensaje":"5 estrellas"},
    2:{"cliente":"Olivia Rubio", "libro":"Nacidos de la bruma", "fecha":"28/04/2024", "mensaje":"2 estrellas"},
}
COMENTARIOS = {
    1:{"cliente":"Nahuel Vicente", "libro":"Harry Potter", "fecha":"27/04/2024", "mensaje":"Muy bueno"},
    2:{"cliente":"Olivia Rubio", "libro":"Nacidos de la bruma", "fecha":"28/04/2024", "mensaje":"Muy malo"},
}
class Notificaciones(Resource):
    def post(self):
        notificacion = request.get_json()
        id = int(max(NOTIFICACIONES.keys()))+1
        NOTIFICACIONES[id] = notificacion 
        return NOTIFICACIONES[id], "mensaje enviado correctamente", 201

class Configuracion(Resource):
    def get(self):
        return CONFIGURACIONES
 
    def put(self):
        if int(id) in CONFIGURACIONES:
            configuracion = CONFIGURACIONES[int(id)]
            data = request.get_json()
            configuracion.update(data)
            return "el mensaje fue actualizado correctamente", 201
        else:
            return 'No existe el id', 404

class Valoracion(Resource):
    def get(self):
        return VALORACIONES
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(VALORACIONES.keys()))+1
        VALORACIONES[id] = prestamo
        return VALORACIONES[id], "La valoracion ha sido registrada correctamente", 201

class Comentarios(Resource):
    def get(self):
        return COMENTARIOS
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(COMENTARIOS.keys()))+1
        COMENTARIOS[id] = prestamo
        return COMENTARIOS[id],"El comentario ha sido registrado correctamente" ,201
    
