import os
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from sqlalchemy.orm import sessionmaker
from app import app, db
#from app.forms import LoginForm, AddRecipe, TagList, UpdateRecipe, AddTag
from app.models import Patient, Doctor, CheckIn
from app import Config
from werkzeug.utils import secure_filename
from datetime import datetime

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    #if session is logged in as doctor, take  to doctor home page
    #if session is logged in as patient, take to patient home page
    #else return login page
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

    return render_template('login.html')

@app.route('/patientcheckin', methods=['GET','POST'])
def patientCheckin():
    if request.method == 'POST':
        checkin = CheckIn(
            tookMed = request.form['tookmed'],
            painLevel = request.form['painlevel'],
            checkInDate = datetime.now()
        )
        return render_template("login.html")
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
            operationDate = str(request.form['operationdate']),
            prescriptionMed = str(request.form["presciptionmedication"]),
            prescriptionDosage = float(request.form["prescriptiondosage"]),
            priorOpioid = int(request.form["prioropioduse"]),
            onAntidepressants = int(request.form["onantidepressants"])
            
        ) 
        db.session.add(patient)
        db.session.commit()
        return redirect(url_for('doctorDashBoard'))

    return render_template("addnewpatient.html")

@app.route('/detailedpatientinfo/<patientid>', methods=['GET','POST'] )
def detailedPatientInfo(patientid):
    patient = Patient.query.filter_by(id=patientid).first_or_404()
    return render_template("detailedpatientinfo.html", patient=patient)
