from flask import Flask, render_template
from api import api
import sqlalchemy
from database import db, test
from config import Config
import os
#init, do not touch
app = Flask(__name__,
template_folder=os.path.abspath(Config.TEMPLATE_FOLDER),
static_folder=os.path.abspath(Config.STATIC_FOLDER))
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()
def querydb(table):
    q = table.query.all()
    return q
@app.route('/')
def hello_world():
    testq=querydb(test)
    print(f"Query result: {testq}")
    print(f"Number of results: {len(testq)}")
    for item in testq:
        print(f"Item ID: {item.id}, huewhg: {item.huewhg}")
    return render_template("index.html")

# Create a namespace for the API
api(app=app)

# API Endpoint

if __name__ == '__main__':
    app.run(debug=True)