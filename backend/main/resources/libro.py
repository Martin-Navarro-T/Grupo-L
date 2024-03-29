from flask_restful import Resource
from flask import request

LIBROS = {
    1:{"titulo":"Fisica II", "editorial":"planeta", "autor":"Ian Lopez"},
    2:{"titulo":"Matematica", "editorial":"hp.edu", "autor":"Martin Olmedo"},
}

class Libro(Resource):
    def get(self,id):
        if int(id) in LIBROS:
            return LIBROS[int(id)] 
        else:
            return "No existe ese libro",404 
        

    def put(self,id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            data = request.get_json()
            return "Actualizado con Exito"
        else:
            "No existe el libro", 404


    def delete(self,id):
        if int(id) in LIBROS:
            del LIBROS[int(id)]
            return "Eliminado con exito"
        else: 
            return "No hay nada para borrar",404
        
class Libros(Resource):
    def get(self):
        return LIBROS
    

    def post(self):

        #ver que dos lbros no se repitan con distintos id 
        libro = request.get_json()
        id = int(max(LIBROS.keys()))+1
        LIBROS[id] = libro
        return LIBROS[id]
    



