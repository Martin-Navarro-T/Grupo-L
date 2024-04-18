from .. import db
from datetime import datetime

class Valoraciones(db.Model):
    id_valoracion = db.Column(db.Integer, primary_key=True)
    id_libros = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)
    valoracion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(100), nullable=False)
    fecha_de_valoración = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        valoracion_json={
            'id_valoracion':self.id_valoracion,
            'id_libros':self.id_libros,
            'id_usuario':self.id_usuario,
            'valoracion':self.valoracion,
            'comentario':str(self.comentario),
            'fecha_de_valoracion':str(self.fecha_de_valoración.strftime("\d-\m-%Y")),
        }
        return valoracion_json

    @staticmethod
    def from_json(valoracion_json):
        id_valoracion = valoracion_json.get("id_valoracion")
        id_libro = valoracion_json.get("id_libro")
        id_usuario = valoracion_json.get("id_usuario")
        valoracion = valoracion_json.get("valoracion")
        comentario = valoracion_json.get("comentario")
        fecha_de_valoracion = valoracion_json("fecha_de_valoracion")
        return Valoraciones(
            id_valoracion = id_valoracion,
            id_libros = id_libro,
            id_usuarios = id_usuario,
            valoracion = valoracion,
            comentario = comentario,
            fecha_de_valoracion = fecha_de_valoracion
        )