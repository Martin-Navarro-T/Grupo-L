from .. import db

class Usuarios(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    #Relación uno a muchos
    configuraciones = db.relationship("Configuracion", back_populates="usuario", cascade="all, delete-orphan")
    #Relación uno a muchos  
    prestamos = db.relationship("Prestamo", back_populates="usuario", cascade="all, delete-orphan")
    # Relación uno a muchos
    valoraciones = db.relationship("Valoraciones", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return '<Usuarios: %r >' % (self.nombre_completo)
    
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

    @staticmethod
    def from_json(usuario_json):
        id_usuario = usuario_json.get("id_usuario")
        nombre_completo = usuario_json.get("nombre_completo")
        direccion = usuario_json.get("direccion")
        dni = usuario_json.get("dni")
        email = usuario_json.get("email")
        password = usuario_json.get("password")
        telefono = usuario_json.get("telefono")
        return Usuarios(
            id_usuario = id_usuario,
            nombre_completo = nombre_completo,
            direccion = direccion,
            dni = dni,
            email = email,
            password = password,
            telefono = telefono
        )

