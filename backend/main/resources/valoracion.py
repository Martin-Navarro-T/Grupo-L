from flask_restful import Resource
from flask import request,jsonify
from .. import db
from main.models import ValoracionesModel
from sqlalchemy import desc, func


class Valoracion(Resource):
    def get(self):
        page = 1

        per_page = 10

        #no ejecuto el .all()
        valoracion = db.session.query(ValoracionesModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        #Filtros
        #Busqueda por libro
        if request.args.get('id_libro'):
            valoracion = valoracion.filter(ValoracionesModel.id_libro == request.args.get('id_libro'))

        #Busqueda por usuario
        if request.args.get('id_usuario'):
            valoracion = valoracion.filter(ValoracionesModel.id_usuario == request.args.get('id_usuario'))

        #Ordenamiento por fecha
        if request.args.get('sortby_fecha_de_valoracion'):
            valoracion = valoracion.order_by(desc(ValoracionesModel.fecha_de_valoracion))

        #Por comentario
        if request.args.get('comentario'):
            valoracion = valoracion.filter(ValoracionesModel.comentario.like("%"+request.args.get('comentario')+"%"))

        #terminan los filtros

        #Paginacion
        valoracion = valoracion.paginate(page=page, per_page=per_page, error_out=False)

        return jsonify({ 'valoraciones': [valoracion.to_json() for valoracion in valoracion.items], 'total': valoracion.total })


        #Anterior
        #valoraciones = db.session.query(ValoracionesModel).all()
        #return jsonify([valoracion.to_json() for valoracion in valoraciones])
    
    def post(self):
        valoracion= ValoracionesModel.from_json(request.get_json())
        print(valoracion)
        try:
            db.session.add(valoracion)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return valoracion.to_json(), 201


#Antes
        #valoracion = ValoracionesModel.from_json(request.get_json())
        #db.session.add(valoracion)
        #db.session.commit()
        #return valoracion.to_json(), 201
