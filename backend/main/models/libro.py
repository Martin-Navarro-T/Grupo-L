from .. import db

class Libro(db.Model):
    id_libro = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    año_de_publicacion = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_json(self):
        libro_json={
            'id_libro':self.id_libro,
            'titulo':str(self.titulo),
            'genero':str(self.genero),
            'editorial':str(self.editorial),
            'año_de_publicacion':self.año_de_publicacion,
            'descripcion':str(self.descripcion),
            'stock':self.stock
        }
        return libro_json