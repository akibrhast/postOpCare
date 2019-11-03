import os
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from app import app, db
from app.models import Patient, Doctor, CheckIn, User
from app import Config
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_login import current_user, login_user, logout_user,login_required
import random
import string
from twilio.rest import Client
from sqlalchemy import create_engine

engine = create_engine('sqlite:///app.db', echo=True)

account_sid = 'ACcc6cce1ce80b883431d71d7414af02b3'
auth_token = '277fa73c21eaaffbb5007f07a63152f3'
client = Client(account_sid, auth_token)

def sendsms(email,password,phonenumber):
    message = client.messages.create(
                     body="Email: "+email+" Password: " + password,
                     from_='+12016854985',
                     to=phonenumber
                 )

    print(message.sid)


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    #if session is logged in as doctor, take  to doctor home page
    #if session is logged in as patient, take to patient home page
    #else return login page
    if request.method == 'POST':
        POST_EMAIL = str(request.form['email'])
        POST_PASSWORD = str(request.form['password'])
        user_all = Patient.query.all()
        user = User.query.filter_by(email=POST_EMAIL).first()
        if user is None or not user.check_password(POST_PASSWORD):
            return render_template('login.html')
        else:
            login_user(user)
            if(user.isDoctor):
                return redirect(url_for('doctorDashBoard'))
            else:
                return redirect(url_for('patientCheckin'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/patientcheckin', methods=['GET','POST'])
@login_required
def patientCheckin():
    if request.method == 'POST':
        patient = Patient.query.filter_by(id=current_user.id).first()
        checkin = CheckIn(
            tookMed = int(request.form['tookmed']),
            painLevel = int(request.form['painlevel']),
            checkInDate = datetime.now(),
            patient = patient
        )
        db.session.add(checkin)
        db.session.commit()
        return render_template("patientcheckin.html")
    return render_template("patientcheckin.html")

@app.route('/doctordashboard')
def doctorDashBoard():
    patients=Patient.query.all()
    return render_template("doctordashboard.html",patients=patients)

@app.route('/addnewpatient', methods=['GET','POST'])
def addNewPatient():
    if request.method == 'POST':
        patient = Patient(
            firstName = str(request.form["firstname"]),
            lastName = str(request.form["lastname"]),
            phoneNumber = str(request.form["phonenumber"]),
            email = str(request.form["email"]),
            operation = str(request.form["operation"]),
            operationDate = datetime.strptime(request.form['operationdate'], '%Y-%m-%d'),
            prescriptionMed = str(request.form["presciptionmedication"]),
            prescriptionDosage = float(request.form["prescriptiondosage"]),
            priorOpioid = int(request.form["prioropioduse"]),
            onAntidepressants = int(request.form["onantidepressants"]),
            password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6)),
            isDoctor = False
        )
        phonenumber='+15715986645'
        patient.password = "a"
        # sendsms(patient.email,patient.password,phonenumber)
        patient.set_password(patient.password)

        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('doctorDashBoard'))

    return render_template("addnewpatient.html")

@app.route('/detailedpatientinfo/<patientid>', methods=['GET','POST'] )
def detailedPatientInfo(patientid):
    patient = Patient.query.filter_by(id=patientid).first_or_404()
    return render_template("detailedpatientinfo.html", patient=patient)
