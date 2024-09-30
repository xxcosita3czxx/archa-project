from flask import Flask, send_from_directory, render_template
from flask_restx import Api, Resource

app = Flask(__name__, static_folder='frontend')
api = Api(app, doc='/swagger')  # Swagger UI at /swagger

# Serve frontend files from 'frontend/' directory as root
@app.route('/')
def hello_world():
    return render_template("frontend\index.html")
  
ns = api.namespace('api', description='API operations')

# API Endpoint
@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)