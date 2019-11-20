from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/api_1')
class API_1(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'post'}


class API_2(Resource):
    def get(self):
        return 'Api 2'

    def post(self):
        return 'api 2 with post'

api.add_resource(API_2, '/api_2')


if __name__ == '__main__':
    app.run(debug=True)