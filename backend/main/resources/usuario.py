from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel, PrestamoModel
from sqlalchemy import func, desc


class Usuario(Resource):
    def get(self,id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return usuario.to_json(), 201
    
    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return 'Ha sido eliminado correctamente', 204
    
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, values in data:
            setattr(usuario, key, values)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201

class Usuarios(Resource):
    def get(self):
        #Página inicial por defecto
        page = 1
        #Cantidad de elementos por página por defecto
        per_page = 10  
        
        #no ejecuto el .all()
        usuarios = db.session.query(UsuarioModel)

        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###
        if request.args.get('nrPrestamos'):
            usuarios=usuarios.outerjoin(UsuarioModel.prestamos).group_by(UsuarioModel.id).having(func.count(PrestamoModel.id) >= int(request.args.get('nrPrestamos')))

        #Busqueda por nombre completo
        if request.args.get('nombre_completo'): #http://127.0.0.1:6003/Usuarios?nombre_completo=Ian
            usuarios=usuarios.filter(UsuarioModel.nombre_completo.like("%"+request.args.get('nombre_completo')+"%"))
        
        #Ordeno por nombre_completo
        if request.args.get('sortby_nombre_completo'):
            usuarios=usuarios.order_by(desc(UsuarioModel.nombre_completo))
            
        ### FIN FILTROS ####
        
        #Obtener valor paginado
        usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                  'total': usuarios.total,
                  'pages': usuarios.pages,
                  'page': page
                })

    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
    
    """    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json() for usuario in usuarios])
    
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201"""