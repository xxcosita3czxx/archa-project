import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'project.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# database.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
