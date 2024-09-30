from flask import Flask, send_from_directory
from api import api

app = Flask(__name__, static_folder='frontend')


# Serve frontend files from 'frontend/' directory as root
@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path='index.html'):
    return send_from_directory(app.static_folder, path)

api(app=app)

if __name__ == '__main__':
    app.run(debug=True)