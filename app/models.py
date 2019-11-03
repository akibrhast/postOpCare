
from app import db, login
import flask_sqlalchemy
from werkzeug.security import check_password_hash, generate_password_hash 
from flask_login import UserMixin

def createDoctors():
    doctorTori = Doctor(
        email = "doctor.tori@email.com",
        password = "a",
        isDoctor = True
    )
    doctorTori.set_password(doctorTori.password)

    doctorAkib = Doctor(
        email = "doctor.akib@email.com",
        password = "a",
        isDoctor = True
    )
    doctorAkib.set_password(doctorAkib.password)

    db.session.add(doctorTori)
    db.session.add(doctorAkib)

    db.session.commit()
    
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(128))
    isDoctor = db.Column(db.Boolean)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Doctor(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    # patient_id = db.Column(db.Integer, db.ForeignKey("doctor.id"))
    # patients = db.relationship("Patient", lazy='dynamic', foreign_keys=['Doctor.id']) # one doctor has many patients

class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tookMed = db.Column(db.Boolean)
    painLevel = db.Column(db.Integer)
    checkInDate = db.Column(db.DateTime)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"))

class Patient(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    phoneNumber = db.Column(db.String(64))
    operation = db.Column(db.String(64))
    operationDate = db.Column(db.Date)
    prescriptionMed = db.Column(db.String(64))
    prescriptionDosage = db.Column(db.Float)
    priorOpioid = db.Column(db.Boolean)
    onAntidepressants = db.Column(db.Boolean)
    addictionRisk = db.Column(db.Integer)
    checkins = db.relationship("CheckIn", backref="patient", lazy='dynamic')
    # doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"))

