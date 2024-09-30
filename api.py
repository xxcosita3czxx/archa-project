from flask_restx import Api, Resource

def api(app):
    api_ns = Api(app, doc='/api/')  # Swagger UI at /swagger

    # Create a namespace for the API
    api = api_ns.namespace('api', description='API operations')

    # API Endpoint
    @api.route('/hello')
    class HelloWorld(Resource):
        def get(self):
            return {'message': 'Hello, World!'}
    
    @api.route("/accounts/create")
    class AccountCreate(Resource):
        def post(self):
            return "making ig...."
    @api.route("/accounts/list")
    class AccountList(Resource):
        def get(self):
            return "listing ig...."

    @api.route("/accounts/delete")
    class AccountDelete(Resource):
        def delete(self):
            return "deleting ig...."
