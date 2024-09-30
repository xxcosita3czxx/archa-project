from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class dbEdit:
    def dumpall(table):
        q = table.query.all()
        return q 
    
class dances(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    task: Mapped[str] = mapped_column(db.String, nullable=False)
class theatres(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    task: Mapped[str] = mapped_column(db.String, nullable=False)
class Visual(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    task: Mapped[str] = mapped_column(db.String, nullable=False)
class musics(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    task: Mapped[str] = mapped_column(db.String, nullable=False)

class test(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    huewhg: Mapped[str] = mapped_column(db.String, nullable=False)

