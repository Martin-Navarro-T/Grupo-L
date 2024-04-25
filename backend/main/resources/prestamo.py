from flask_restful import Resource
from flask import request, jsonify
from .. import db
from datetime import datetime
from main.models import PrestamoModel
from sqlalchemy import extract, desc

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
        page = 1
        per_page = 10

        id_usuario = request.args.get('id_usuario')
        filters = request.args.to_dict()

        prestamos = db.session.query(PrestamoModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        if id_usuario:
            prestamos = prestamos.filter(PrestamoModel.id_usuario == id_usuario)
            
        if filters:
            for key, value in filters.items():
                if key == "id_usuario":
                    prestamos = prestamos.filter(PrestamoModel.id_usuario == value)
                elif key == "fecha_de_entrega":
                    if value.startswith('-'):
                        month = value.lstrip('-')
                        prestamos = prestamos.filter(
                            extract('month', PrestamoModel.fecha_de_entrega) == int(month)
                        )
                    elif len(value) == 2:
                        prestamos = prestamos.filter(
                            extract('day', PrestamoModel.fecha_de_entrega) == int(value)
                        )
                    elif len(value) == 4:
                        prestamos = prestamos.filter(
                            extract('year', PrestamoModel.fecha_de_entrega) == int(value)
                        )
                    else:
                        prestamos=prestamos.filter(PrestamoModel.fecha_de_entrega.like("%"+value+"%"))
                elif key == "fecha_de_vencimiento":
                    if value.startswith('-'):
                        month = value.lstrip('-')
                        prestamos = prestamos.filter(
                            extract('month', PrestamoModel.fecha_de_vencimiento) == int(month)
                        )
                    elif len(value) == 2:
                        prestamos = prestamos.filter(
                            extract('day', PrestamoModel.fecha_de_vencimiento) == int(value)
                        )
                    elif len(value) == 4:
                        prestamos = prestamos.filter(
                            extract('year', PrestamoModel.fecha_de_vencimiento) == int(value)
                        )
                    else:
                        prestamos=prestamos.filter(PrestamoModel.fecha_de_vencimiento.like("%"+value+"%"))

        if request.args.get('id_prestamo'):
            prestamos = prestamos.filter(PrestamoModel.id_prestamo == value)

        if request.args.get('sortby_id_prestamo'):
            prestamos=prestamos.order_by(desc(PrestamoModel.id_prestamo))

        if request.args.get('id_usuario'):
            prestamos = prestamos.filter(PrestamoModel.id_usuario == value)

        if request.args.get('sortby_id_usuario'):
            prestamos=prestamos.order_by(desc(PrestamoModel.id_usuario))

        if request.args.get('id_libros'):
            prestamos = prestamos.filter(PrestamoModel.id_libros == value)

        if request.args.get('sortby_id_libros'):
            prestamos=prestamos.order_by(desc(PrestamoModel.id_libros))

        if request.args.get('sortby_fecha_de_entrega'):
            prestamos=prestamos.order_by(desc(PrestamoModel.fecha_de_entrega))
        
        if request.args.get('sortby_fecha_de_vencimiento'):
            prestamos=prestamos.order_by(desc(PrestamoModel.fecha_de_vencimiento))

        if request.args.get('estado'):
            prestamos = prestamos.filter(PrestamoModel.estado == value)

        prestamos = prestamos.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'prestamos': [prestamo.to_json() for prestamo in prestamos.items],
                  'total de prestamos': prestamos.total,
                  'paginas': prestamos.pages,
                  'pagina': page
                })
    
    def post(self):
        prestamo = PrestamoModel.from_json(request.get_json())
        print(prestamo)
        try:
            db.session.add(prestamo)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return prestamo.to_json(), 201