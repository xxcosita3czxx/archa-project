from flask_restx import Api, Resource

def api(app):
    api = Api(app, doc='/api/docs')  # Swagger UI at /swagger

    # Create a namespace for the API
    ns = api.namespace('api', description='API operations')

    # API Endpoint
    @ns.route('/api/hello')
    class HelloWorld(Resource):
        def get(self):
            return {'message': 'Hello, World!'}
