from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
db = SQLAlchemy(app)

class Student(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    sname = db.Column(db.String(50), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    year = db.Column(db.String(10), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
