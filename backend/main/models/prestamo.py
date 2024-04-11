from .. import db

class Prestamo(db.Model):
    id_prestamo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    id_libros = db.Column(db.Integer, nullable=False)
    fecha_de_prestamo = db.Column(db.Date, nullable=False) #fecha de entrega
    fecha_de_vencimiento = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(100), nullable=False)


    def to_json(self):
        usuario_json={
            'id_prestamo':self.id_prestamo,
            'id_usuario':self.id_usuario,
            'id_libros':self.id_libros,
            'fecha_de_prestamo':str(self.fecha_de_prestamo),
            'fecha_de_vencimiento':str(self.fecha_de_vencimiento),
            'estado':str(self.estado),
        }
        return usuario_json
