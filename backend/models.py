from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    senha = db.Column(db.String(80), nullable=False)

class Postagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(80), nullable=False)
    texto = db.Column(db.Text, nullable=False)
    nome_autor = db.Column(db.String(50), nullable=False)
    datahora_postagem = db.Column(db.DateTime, nullable=False)