import os
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
#from sqlalchemy.orm import sessionmaker
from app import app, db
#from app.forms import LoginForm, AddRecipe, TagList, UpdateRecipe, AddTag
#from app.models import Recipe, Tag, recipeTag
from app import Config
from werkzeug.utils import secure_filename


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

@app.route('/patientcheckin')
def patientCheckin():
    return render_template("patientcheckin.html")
@app.route('/doctordashboard')
def doctorDashBoard():
    patients=[{
        "Akib",
        "Rahman",
        "01/02/2018",
        "1500",
        "Cataract Surgery",
        "DETAILED SURGERY INFORMATION Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut sapien eros, pellentesque quis maximus a, rutrum quis ex. Duis aliquet diam et erat scelerisque, et blandit velit posuere. Maecenas eros est, lobortis vitae tincidunt et, molestie sit amet nunc. Nam magna elit, sodales vitae venenatis non, fermentum in dui. Vestibulum nec risus nibh. Sed scelerisque ultricies leo, et blandit nulla ornare eu. Morbi felis mauris, euismod a tincidunt mattis, pharetra eu nulla. Sed posuere semper felis eu pharetra.",
        },{
        "Akib",
        "Rahman",
        "01/02/2018",
        "1500",
        "Cataract Surgery",
        "DETAILED SURGERY INFORMATION Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut sapien eros, pellentesque quis maximus a, rutrum quis ex. Duis aliquet diam et erat scelerisque, et blandit velit posuere. Maecenas eros est, lobortis vitae tincidunt et, molestie sit amet nunc. Nam magna elit, sodales vitae venenatis non, fermentum in dui. Vestibulum nec risus nibh. Sed scelerisque ultricies leo, et blandit nulla ornare eu. Morbi felis mauris, euismod a tincidunt mattis, pharetra eu nulla. Sed posuere semper felis eu pharetra.",
        },{
        "Akib",
        "Rahman",
        "01/02/2018",
        "1500",
        "Cataract Surgery",
        "DETAILED SURGERY INFORMATION Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut sapien eros, pellentesque quis maximus a, rutrum quis ex. Duis aliquet diam et erat scelerisque, et blandit velit posuere. Maecenas eros est, lobortis vitae tincidunt et, molestie sit amet nunc. Nam magna elit, sodales vitae venenatis non, fermentum in dui. Vestibulum nec risus nibh. Sed scelerisque ultricies leo, et blandit nulla ornare eu. Morbi felis mauris, euismod a tincidunt mattis, pharetra eu nulla. Sed posuere semper felis eu pharetra.",
        }]
    return render_template("doctordashboard.html",patients=patients)

@app.route('/addnewpatient')
def addNewPatient():
    #Create new patient, and send sms/email to patient with username and temp password and website url
    return render_template("addnewpatient.html")

@app.route('/detailedpatientinfo')
def detailedPatientInfo():
    return render_template("detailedpatientinfo.html")
