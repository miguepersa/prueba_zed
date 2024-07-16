import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Saludo(db.Model):
    __tablename__ = "saludos"

    id = Column(Integer, primary_key=True)
    mensaje = Column(String(128), nullable=False)

    def __init__(self, mensaje):
        self.mensaje = mensaje

    @property
    def serialize(self):
        return {
            "id" : self.id,
            "mensaje" : self.mensaje
        }
    

def crear_saludo():
    data = request.json
    mensaje = data.get("mensaje")

    saludo = Saludo(
        mensaje = mensaje
    )
    db.session.add(saludo) 
    db.session.commit()

    return jsonify(saludo.serialize)

def listar_saludos():
    saludos = Saludo.query.all()
    return jsonify([s.serialize for s in saludos])


@app.route('/saludos', methods=["GET", "POST"])
def saludos():
    if request.method == 'GET': 
        return listar_saludos()
    if request.method == 'POST': 
        return crear_saludo()


@app.route('/saludos/<saludo_id>', methods=["GET"])
def obtener_saludo(saludo_id):
    saludo = Saludo.query.get(saludo_id)
    return jsonify(saludo.serialize)