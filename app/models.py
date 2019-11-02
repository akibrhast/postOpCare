from app import db

class Patient(db.Model):
    id = db.Column(db.IntegerField, primary_key=True)
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    operation = db.Column(db.String(64))
    prescriptionMed = db.Column(db.String(64))
    prescriptionDosage = db.Column(db.Float)
    priorOpioid = db.Column(db.Boolean)
    onAntidepressants = db.Column(db.Boolean)
    addictionRisk = db.Column(db.Integer)
    checkIns = db.relationship('CheckIn', backref='patient')


class CheckIn(db.Model):
    id = db.Column(db.IntegerField, primary_key=True)
    patientId = db.Column(db.IntegerField, db.ForeignKey('patient.id'))
    tookMed = db.Column(db.Boolean)
    painLevel = db.Column(db.Integer)
    checkInDate = db.Column(db.DateTime)