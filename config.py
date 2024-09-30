import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
class Config:
    TEMPLATE_FOLDER = "frontend/"
    STATIC_FOLDER = "frontend/"
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, 'project.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
print(Config.SQLALCHEMY_DATABASE_URI)
