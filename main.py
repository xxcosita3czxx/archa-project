from flask import Flask, render_template, make_response, request, jsonify
from random_word import RandomWords
import random
from api import api
from sqlalchemy import delete
from database import db, dances, theatres, Visual, musics, images
from config import Config
import os
import requests
from PIL import Image
import numpy as np
from io import BytesIO
from skimage.metrics import structural_similarity as ssim
import click
from datetime import datetime


#init, do not touch
app = Flask(
    __name__,
    template_folder=os.path.abspath(Config.TEMPLATE_FOLDER),
    static_folder=os.path.abspath(Config.STATIC_FOLDER)
)

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
    current = images.query.first()
    nowtime = datetime.now()
    if not current:
        print("not current")
        nowtime = nowtime.replace(hour=23, minute=59, second=59, microsecond=0)
        prompt = ""
        r = RandomWords()
        for i in range(random.randrange(1,5)):
            prompt += r.get_random_word() + "_"
        delete_stmt = delete(images).where(images.id == 1)
        db.session.execute(delete_stmt)
        newprompt = images(
            enddate=nowtime,
            prompt = prompt
        )
        db.session.add(newprompt)
    else:
        endtime = endtime = datetime.strptime(current.enddate, "%Y-%m-%d %H:%M:%S")
        if endtime < nowtime:
            print("the end is nigh")
            nowtime = nowtime.replace(hour=23, minute=59, second=59, microsecond=0)
            prompt = "" 
            r = RandomWords()
            for i in range(random.randrange(1,5)):
                prompt += r.get_random_word() + "_"
            delete_stmt = delete(images).where(images.id == 1)
            db.session.execute(delete_stmt)
            newprompt = images(
                enddate=nowtime,
                prompt = prompt
            )
            db.session.add(newprompt)
    db.session.commit()
    current = images.query.first()
    prompt = current.prompt
    context = {
        "dayprompt":prompt
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
    adjusted_similarity_percentage = adjusted_similarity * 250
    if adjusted_similarity_percentage >= 101:
        adjusted_similarity_percentage = 101
    return jsonify({
        "similarity": f"{adjusted_similarity_percentage:.2f}%",  
        "message": "Images processed successfully."
    })


@click.command()
@click.option("--debug",is_flag=True)
@click.option("--port")
@click.option("--ip")
@click.option("--cert")
@click.option("--key")
def main(debug,cert,key,port=5000,ip="127.0.0.1"):
    if debug:
        if cert and key:
            context = (cert, key)
            app.run(debug=True,port=port,host=ip,ssl_context=context)
        else:
            app.run(debug=True,port=port,host=ip)
    else:
        if cert and key:
            context = (cert, key)
            app.run(port=port,host=ip,ssl_context=context)
        else:
            app.run(port=port,host=ip)

if __name__ == '__main__':
    main()
