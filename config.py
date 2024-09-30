import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TEMPLATE_FOLDER = "frontend/"
    STATIC_FOLDER = "frontend/"
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# database.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
