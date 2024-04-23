from flask_restful import Resource
from flask import request, jsonify
from .. import db
from datetime import datetime
from main.models import PrestamoModel

#post crea y put actualiza

class Prestamo(Resource):
    def get(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        return prestamo.to_json(), 201
    
    def delete(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return 'El prestamo fue eliminado correctamente', 204
    
    def put(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            if key == 'fecha_de_entrega':
                fecha_de_entrega = datetime.strptime(value, '%d-%m-%Y')
                setattr(prestamo, key, fecha_de_entrega)
            elif key == 'fecha_de_vencimiento':
                fecha_de_vencimiento = datetime.strptime(value, '%d-%m-%Y')
                setattr(prestamo, key, fecha_de_vencimiento)
            else:
                setattr(prestamo, key, value)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201


class Prestamos(Resource):
    def get(self):
        #Obtener valores del request
        id_usuario = request.args.get('id_usuario')
        
        prestamos = db.session.query(PrestamoModel)
        
        #Verificar si hay filtros
        if id_usuario:
            prestamos = prestamos.filter(PrestamoModel.id_usuario == id_usuario)
        # if filters:
        #     #Recorrer filtros
        #     for key, value in request.get_json().items():
        #         if key == "id_usuario":
        #             prestamos = prestamos.filter(PrestamoModel.id_usuario == value)
        
        
        #finalmete con los filtros aplicados hago el all
        #tambien se puede manejar la paginacion
        prestamos = prestamos.all()

        return jsonify({ 'prestamos': [prestamo.to_json() for prestamo in prestamos] })
    
"""    def get(self):
        prestamos = db.session.query(PrestamoModel).all()
        return jsonify([prestamo.to_json() for prestamo in prestamos])
    
    def post(self):
        prestamo = PrestamoModel.from_json(request.get_json())
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201"""
    
