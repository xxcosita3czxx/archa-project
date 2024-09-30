from flask import Flask, send_from_directory, render_template
from api import api

app = Flask(__name__, static_folder='frontend')


# Serve frontend files from 'frontend/' directory as root
@app.route('/')
def hello_world():
    return render_template("index.html")

# Create a namespace for the API
ns = api.namespace('api', description='API operations')

# API Endpoint
@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)