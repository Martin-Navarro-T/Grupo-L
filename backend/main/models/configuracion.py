from .. import db

class Configuracion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    configuracion = db.Column(db.String(100), nullable=False)
    caracteristicas = db.Column(db.String(100), nullable=False)

    def to_json(self):
        configuracion_json={
            'id':self.id,
            'configuracion':str(self.configuracion),
            "caracteristicas":str(self.caracteristicas),
        }
        return configuracion_json
    
class Configuraciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def to_json(self):
        configuracion_json={
            'id':self.id,
            'nombre':str(self.nombre),
        }
        return configuracion_json

