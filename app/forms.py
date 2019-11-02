# Not in use
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class  LoginForm:
    pass

class AddPatient(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    operation = StringField('Operation', validators=[DataRequired()])
    prescriptionMed = StringField("Perscription Med", validators=(DataRequired()))
    prescriptionDosage = FloatField()
    priorOpioid = BooleanField("Prior Opioid User")
    onAntidepressants = BooleanField('On Antidepressants')
    submit = SubmitField


class AddCheckIn(FlaskForm):
    tookMed = BooleanField("Took Medication?")
    painLevel = IntegerField("Pain Level")
