from .. import db

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(100), nullable=False)
    id_usuario = db.Column(db.Integer, forance_key=True)

    def to_json(self):
        comentario_json={
            'id':self.id,
            'comentario':str(self.comentario),
            "id_usuario":self.id_usuario
        }
        return comentario_json
    
    