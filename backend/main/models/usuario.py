from .. import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)

    def to_json(self):
        usuario_json={
            'id_usuario':self.id_usuario,
            'nombre_completo':str(self.nombre_completo),
            'direccion':str(self.direccion),
            'dni':self.dni,
            'email':str(self.email),
            'password':str(self.password),
            'telefono':self.telefono
        }
        return usuario_json
    