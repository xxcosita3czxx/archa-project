from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()
def querydb(table):
    q = table.query.all()
    return q
class test(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    huewhg: Mapped[str] = mapped_column(db.String, nullable=False)

