from flask import Flask, render_template, make_response, request, jsonify, send_from_directory, redirect
from api import api
import sqlalchemy
from database import db, test, dances, theatres, Visual, musics, images
from config import Config
import os
import requests
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
from skimage.metrics import structural_similarity as ssim
import random
import click

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
    finaldance = ""
    for i in dancesq:
        if "linktarger=" in i.task:
            cont = i.task
            cont = cont.split("linktarger=")
            print(cont)
            link="<a href = \\\""+ cont[1] + "\\\">(click)" + "</a>"
            finaldancetemp = cont[0] + link
            finaldance += "\""+finaldancetemp+"\",\n"
            print(link)
            print(finaldance)
        else:
            dancesl.append(i.task)
    theatresl = []
    theatresq = theatres.query.all()
    finaltheatre = ""
    for i in theatresq:
        if "linktarger=" in i.task:
            cont = i.task
            cont = cont.split("linktarger=")
            print(cont)
            link="<a href = \\\""+ cont[1] + "\\\">(click)" + "</a>"
            finaltheatretemp = cont[0] + link
            finaltheatre += "\""+finaltheatretemp+"\",\n"
            print(link)
            print(finaltheatre)
        else:
            theatresl.append(i.task)
    visualsl = []
    visualsq = Visual.query.all()
    finalvisual = ""
    for i in visualsq:
        if "linktarger=" in i.task:
            cont = i.task
            cont = cont.split("linktarger=")
            print(cont)
            link="<a href = \\\""+ cont[1] + "\\\">(click)" + "</a>"
            finalvisualtemp = cont[0] + link
            finalvisual += "\""+finalvisualtemp+"\",\n"
            print(link)
            print(finalvisual)
        else:    
            pass
            visualsl.append(i.task)
    musicsl = []
    musicsq = musics.query.all()
    finalmusic = ""
    for i in musicsq:
        if "linktarger=" in i.task:
            cont = i.task
            cont = cont.split("linktarger=")
            print(cont)
            link="<a href = \\\""+ cont[1] + "\\\">(click)" + "</a>"
            finalmusictemp = cont[0] + link
            finalmusic += "\""+finalmusictemp+"\",\n"
            print(link)
            print(finalmusic)
        else:
            musicsl.append(i.task)
    context = {
        "dances":dancesl,
        "theatres": theatresl,
        "visuals": visualsl,
        "musics": musicsl,
    }
    
    resp = make_response(render_template("kolo.html",finalvisual = finalvisual, finalmusic = finalmusic, finaldance = finaldance, finaltheatre = finaltheatre , **context))
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
    imgs = images.query.all()
    imgsl = []
    for i in imgs:
        imgsl.append(i.link)
    img = random.choice(imgsl)
    context = {
        "img":img
    }
    
    resp = make_response(render_template("day.html", **context))
    return resp 
# Create a namespace for the API
api(app=app)
"""@app.route('/upload', methods=['POST'])
def upload():
    if 'canvas_image' not in request.files or 'original_image' not in request.form:
        return jsonify({"error": "Missing required files"}), 400

    canvas_image = Image.open(request.files['canvas_image']).convert('L')  # Convert to grayscale
    original_image_url = request.form['original_image']
    
    # Download and open the original image
    response = requests.get(original_image_url)
    original_image = Image.open(BytesIO(response.content)).convert('L')  # Convert to grayscale
    
    # Resize images to match
    size = (50, 50)  # You can adjust this size as needed
    canvas_image = canvas_image.resize(size)
    original_image = original_image.resize(size)

    # Convert images to numpy arrays
    canvas_array = np.array(canvas_image)
    original_array = np.array(original_image)
    canvas_filled_ratio = np.sum(canvas_array < 240) / canvas_array.size
    if canvas_filled_ratio < 0.05:
        return jsonify({
            "similarity": "0.00%",
            "message": "Your canvas appears to be blank or nearly blank. Try drawing something!"
        })
    # Calculate the Mean Squared Error (MSE)
    similarity, _ = ssim(canvas_array, original_array, full=True)
    brightness_diff = abs(np.mean(canvas_array) - np.mean(original_array)) / 255
    adjusted_similarity = similarity * (1 - brightness_diff)
    
    # Convert similarity to percentage
    adjusted_similarity = similarity * 750
    print(adjusted_similarity)
    return redirect("/drawing")
# API Endpoint"""

@app.route('/upload', methods=['POST'])
def upload():
    if 'canvas_image' not in request.files or 'original_image' not in request.form:
        return jsonify({"error": "Missing required files"}), 400

    canvas_image = Image.open(request.files['canvas_image']).convert('L')  # Convert to grayscale
    original_image_url = request.form['original_image']
    
    # Download and open the original image
    response = requests.get(original_image_url)
    original_image = Image.open(BytesIO(response.content)).convert('L')  # Convert to grayscale
    
    # Resize images to match
    size = (50, 50)  # You can adjust this size as needed
    canvas_image = canvas_image.resize(size)
    original_image = original_image.resize(size)

    # Convert images to numpy arrays
    canvas_array = np.array(canvas_image)
    original_array = np.array(original_image)
    canvas_filled_ratio = np.sum(canvas_array < 240) / canvas_array.size
    if canvas_filled_ratio < 0.05:
        return jsonify({
            "similarity": "0.00%",
            "message": "Your canvas appears to be blank or nearly blank. Try drawing something!"
        })

    # Calculate the Mean Squared Error (MSE)
    similarity, _ = ssim(canvas_array, original_array, full=True)
    brightness_diff = abs(np.mean(canvas_array) - np.mean(original_array)) / 255
    adjusted_similarity = similarity * (1 - brightness_diff)
    
    # Convert similarity to percentage
    adjusted_similarity_percentage = adjusted_similarity * 250  # To convert to percentage

    return jsonify({
        "similarity": f"{adjusted_similarity_percentage:.2f}%",  # Format similarity to 2 decimal places
        "message": "Images processed successfully."
    })


@click.command()
@click.option("--debug",is_flag=True)
@click.option("--port")
def main(debug,port=5000):
    if debug:
        app.run(debug=True,port=port)
    else:
        app.run(port=port)

if __name__ == '__main__':
    main()
