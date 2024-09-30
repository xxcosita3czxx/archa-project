from flask import Flask, render_template, make_response
from api import api
import sqlalchemy
from database import db, test, dances, theatres, Visual, musics
from config import Config
import os

#TODO Neural Network image check


#init, do not touch
app = Flask(__name__,
template_folder=os.path.abspath(Config.TEMPLATE_FOLDER),
static_folder=os.path.abspath(Config.STATIC_FOLDER))
app.config.from_object(Config)
db.init_app(app)

@app.route('/kolo')
def kolo():
    dancesl = []
    dancesq = dances.query.all()
    for i in dancesq:
        print(i.task)
        dancesl.append(i.task)
    theatresl = []
    theatresq = theatres.query.all()
    for i in theatresq:
        print(i.task)
        theatresl.append(i.task)
    visualsl = []
    visualsq = Visual.query.all()
    for i in visualsq:
        print(i.task)
        visualsl.append(i.task)
    musicsl = []
    musicsq = musics.query.all()
    for i in musicsq:
        print(i.task)
        musicsl.append(i.task)
    context = {
        "dances":dancesl,
        "theatres": theatresl,
        "visuals": visualsl,
        "musics": musicsl,
    }
    
    resp = make_response(render_template("kolo.html", **context))
    return resp 
@app.route('/')
def index():
    resp = make_response(render_template("index.html"))
    return resp 
@app.route('/drawing')
def drawing():
    resp = make_response(render_template("drawing.html"))
    return resp 
@app.route('/day')
def day():
    resp = make_response(render_template("day.html"))
    return resp 
# Create a namespace for the API
api(app=app)

# API Endpoint

if __name__ == '__main__':
    app.run(debug=True)