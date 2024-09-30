from flask import Flask, render_template, make_response
from api import api
import sqlalchemy
from database import db, test, dances
from config import Config
import os

#TODO Neural Network image check


#init, do not touch
app = Flask(__name__,
template_folder=os.path.abspath(Config.TEMPLATE_FOLDER),
static_folder=os.path.abspath(Config.STATIC_FOLDER))
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def hello_world():
    dancesl = []
    dancesq = dances.query.all()
    for i in dancesq:
        print(i.task)
        dancesl.append(i.task)
    context = {
        "dances":dancesl,
        "tst":"tst"
    }
    
    resp = make_response(render_template("kolo.html", **context))
    return resp 

# Create a namespace for the API
api(app=app)

# API Endpoint

if __name__ == '__main__':
    app.run(debug=True)