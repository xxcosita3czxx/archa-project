from flask import Flask, send_from_directory
from flask_restx import Api, Resource

app = Flask(__name__, static_folder='frontend')
api = Api(app, doc='/swagger')  # Swagger UI at /swagger

# Serve frontend files from 'frontend/' directory as root
@app.route('/')
@app.route('/<path:path>')
def serve_frontend(path='index.html'):
    return send_from_directory(app.static_folder, path)

# Create a namespace for the API
ns = api.namespace('api', description='API operations')

# API Endpoint
@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)