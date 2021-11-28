from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class SentimentalAnalysis(Resource):
    def get(self):
        return jsonify({'hello': 'world'})

api.add_resource(SentimentalAnalysis, '/')

if __name__ == '__main__':
    app.run(debug=True)