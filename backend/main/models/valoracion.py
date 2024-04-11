from .. import db

class Valoraciones(db.Model):
    id_valoracion = db.Column(db.Integer, primary_key=True)
    id_libros = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)
    valoracion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(100), nullable=False)
    fecha_de_valoración = db.Column(db.Date, nullable=False)

    def to_json(self):
        usuario_json={
            'id_valoracion':self.id_valoracion,
            'id_libros':self.id_libros,
            'id_usuario':self.id_usuario,
            'valoracion':self.valoracion,
            'comentario':str(self.comentario),
            'fecha_de_valoracion':str(self.fecha_de_valoración),
        }
        return usuario_json
    