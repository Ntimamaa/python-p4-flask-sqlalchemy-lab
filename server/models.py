from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
from app import db

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeeper.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosure.id'))

class Zookeeper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.DateTime, default=datetime.utcnow)
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)

class Enclosure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(100), nullable=False)
    open_to_visitors = db.Column(db.Boolean, default=True)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)

