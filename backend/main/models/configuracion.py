from .. import db

class Configuracion(db.Model):
    id_configuracion = db.Column(db.Integer, primary_key=True)
    nombre_configuracion = db.Column(db.String(100), nullable=False)
    valor_configuracion = db.Column(db.String(100), nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)


    def to_json(self):
        configuracion_json={
            'id_configuracion':self.id,
            'nombre_configuracion':str(self.nombre_configuracion),
            "valor_configuracion":str(self.valor_configuracion),
            "id_usuario":self.id_usuario
        }
        return configuracion_json
    
    def from_json(configuracion_json):
        id_configuracion = configuracion_json.get("id_configuracion")
        nombre_configuracion = configuracion_json.get("nombre_configuracion")
        id_usuario = configuracion_json.get("id_usuario")
        valor_configuracion = configuracion_json.get("valor_configuracion")
        
        return Configuracion(
            id_configuracion = id_configuracion,
            nombre_configuracion = nombre_configuracion,
            id_usuario = id_usuario,
            valor_configuracion = valor_configuracion
        )

        


"""
class Configuraciones(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def to_json(self):
        configuracion_json={
            'id':self.id,
            'nombre':str(self.nombre),
        }
        return configuracion_json
"""


