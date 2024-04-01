from flask_restful import Resource
from flask import request

CUENTAS = {
    1:{"nombre":"Nahuel Vicente", "telefono":"26155432", "email":"nahuel2001@gmail.com"},
    2:{"nombre":"Olivia Rubio", "telefono":"261909451", "email":"o.rubia34@gmail.com"},
}

class Sign_in(Resource):
    def post (self):
        cuenta = request.get_json()
        id = int(max(CUENTAS.keys()))+1
        CUENTAS[id] = cuenta
        return "La cuenta ha sido creada con exito!"
    
class Login(Resource):
    def post (self):
        cuenta = request.get_json()
        id = int(max(CUENTAS.keys()))+1
        CUENTAS[id] = cuenta
        return "Ha podido iniciar sesión!"

