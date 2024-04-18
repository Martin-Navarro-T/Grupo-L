from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import LibroModel


class Libro(Resource):
    def get(self,id):
    
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json(), 201 
        
    def put(self,id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json() , 201


    def delete(self,id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return "El libro fue eliminado correctamente", 204
    
    

class Libros(Resource):
    def get(self):
        libros = db.session.query(LibroModel).all()
        return jsonify([libro.to_json() for libro in libros])

    def post(self):
        libro = LibroModel.from_json(request.get_json())
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201






