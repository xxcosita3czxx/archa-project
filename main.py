from flask import Flask, render_template
from api import api

app = Flask(__name__, static_folder='./frontend', template_folder='./frontend')


# Serve frontend files from 'frontend/' directory as root
@app.route('/')
def hello_world():
    return render_template("index.html")

# Create a namespace for the API
api(app=app)

# API Endpoint

if __name__ == '__main__':
    app.run(debug=True)