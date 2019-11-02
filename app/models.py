
from app import db
import flask_sqlalchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

class Doctor(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    # patient = db.relationship("Patient", backref='doctor')

class Patient(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    phoneNumber = db.Column(db.String(64))
    email = db.Column(db.String(64))
    operation = db.Column(db.String(64))
    operationDate = db.Column(db.Date)
    prescriptionMed = db.Column(db.String(64))
    prescriptionDosage = db.Column(db.Float)
    priorOpioid = db.Column(db.Boolean)
    onAntidepressants = db.Column(db.Boolean)
    addictionRisk = db.Column(db.Integer)
    # checkin = db.relationship("CheckIn", backref='patient')
    
class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tookMed = db.Column(db.Boolean)
    painLevel = db.Column(db.Integer)
    checkInDate = db.Column(db.DateTime)
