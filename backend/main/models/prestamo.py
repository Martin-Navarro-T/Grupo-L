from .. import db

class Prestamo(db.Model):
    id_prestamo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    id_libros = db.Column(db.Integer, nullable=False)
    fecha_de_entrega = db.Column(db.DateTime, nullable=False) 
    fecha_de_vencimiento = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.String(100), nullable=False)

    #Convertir objeto en JSON
    def to_json(self):
        prestamo_json={
            'id_prestamo':self.id_prestamo,
            'id_usuario':self.id_usuario,
            'id_libros':self.id_libros,
            'fecha_de_entrega':str(self.fecha_de_entrega.strftime("\d-\m-%Y")),
            'fecha_de_vencimiento':str(self.fecha_de_vencimiento.strftime("\d-\m-%Y")),
            'estado':str(self.estado),
        }
        return prestamo_json

    def to_json_short(self):
        prestamo_json = {
            'id_prestamo':self.id_prestamo,
            'id_usuario':self.id_usuario,
            'id_libros':self.id_libros,
            'fecha_de_entrega':str(self.fecha_de_entrega),
            'fecha_de_vencimiento':str(self.fecha_de_vencimiento),
            'estado':str(self.estado),
        }
        return prestamo_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(prestamo_json):
        id_prestamo = prestamo_json.get('id_prestamo')
        id_usuario = prestamo_json.get('id_usuario')
        id_libros = prestamo_json.get('id_libros')
        fecha_de_prestamo = prestamo_json.get('fecha_de_prestamo')
        fecha_de_vencimiento = prestamo_json.get('fecha_de_vencimiento')
        estado = prestamo_json.get('estado')
        return Prestamo(id_prestamo=id_prestamo,
                    id_usuario=id_usuario,
                    id_libros=id_libros,
                    fecha_de_prestamo=fecha_de_prestamo,
                    fecha_de_vencimiento=fecha_de_vencimiento,
                    estado=estado
                    )
