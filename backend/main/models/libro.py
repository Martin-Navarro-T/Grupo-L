from .. import db
from datetime import datetime

class Libro(db.Model):
    id_libro = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    año_de_publicacion = db.Column(db.DateTime, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_json(self):
        libro_json={
            'id_libro':self.id_libro,
            'titulo':str(self.titulo),
            'genero':str(self.genero),
            'editorial':str(self.editorial),
            'año_de_publicacion':str(self.año_de_publicacion.strftime("%d-%m-%Y")),
            'descripcion':str(self.descripcion),
            'stock':self.stock
        }
        return libro_json
    
    
    """""
    def to_json_short(self):
        libro_json = {
            'id_libro':self.id_libro,
            'titulo':str(self.titulo),
            'genero':str(self.genero),
            'editorial':str(self.editorial),
            'año_de_publicacion':self.año_de_publicacion,
            'descripcion':str(self.descripcion),
            'stock':self.stock
        }
        return libro_json
    """""
   

    
    def from_json(libro_json):
        id_libro = libro_json.get('id_libro')
        titulo = libro_json.get('titulo')
        genero = libro_json.get('genero')
        editorial = libro_json.get('editorial')
        año_de_publicacion = datetime.strptime(libro_json.get('año_de_publicacion'), '%d-%m-%Y')
        descripcion = libro_json.get('descripcion')
        stock = libro_json.get('stock')
        return Libro(id_libro=id_libro,
                    titulo=titulo,
                    genero=genero,
                    editorial=editorial,
                    año_de_publicacion=año_de_publicacion,
                    descripcion=descripcion,
                    stock=stock,
                    )