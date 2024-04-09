from .. import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def to_json(self):
        usuario_json={
            'id':self.id,
            'nombre':str(self.nombre)
        }
        return usuario_json