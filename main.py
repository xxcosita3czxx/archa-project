from flask import Flask, render_template, make_response,request,jsonify, send_from_directory, redirect
from api import api
import sqlalchemy
from database import db, test, dances, theatres, Visual, musics
from config import Config
import os
import requests
from PIL import Image
from io import BytesIO
from werkzeug.datastructures import FileStorage

from PIL import Image
#TODO Neural Network image check


#init, do not touch
app = Flask(__name__,
template_folder=os.path.abspath(Config.TEMPLATE_FOLDER),
static_folder=os.path.abspath(Config.STATIC_FOLDER))
app.config.from_object(Config)
db.init_app(app)
def get_image_from_url(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
    # Create an image object from the downloaded data
        image = Image.open(BytesIO(response.content))
        image_buffer = BytesIO()
        image.save(image_buffer, format='JPEG')
        image_buffer.seek(0)
        file_storage = FileStorage(image_buffer, filename="drawing.jpg", content_type="image/jpeg")
        return file_storage
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
@app.route('/upload', methods=['POST'])
def upload():
    if 'canvas_image' in request.files:
        canvas_image = request.files['canvas_image']
        print(canvas_image)
        
    if 'original_image' in request.form:
        original_image_url = request.form['original_image']
        print(f"Original image URL: {original_image_url}")
    print(get_image_from_url(original_image_url))
    image = Image.open(get_image_from_url(original_image_url)   )
    image.show()
    background = Image.open(get_image_from_url(original_image_url))
    overlay = Image.open(canvas_image)

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.5)
    image = Image.open(new_img)
    image.show()
    return redirect("/drawing")
# API Endpoint

if __name__ == '__main__':
    app.run(debug=True)