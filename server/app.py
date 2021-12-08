from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from services.loader import Loader

app = Flask(__name__)
CORS(app)
api = Api(app)

class SentimentalAnalysis(Resource):
    def __init__(self):
        self.loader = Loader()

    def get(self):
        data = {
            "sentimental": self.loader.get_sentimentals_of_all_airlines(),
            "airlines": self.loader.get_airline_count(),
            "negative_test": self.loader.get_negative_reason_count(),
            "null_values_from_columns": self.loader.get_null_values_from_all_columns(),
            "accuracy": self.loader.get_accuracy_for_models()
        }
        return jsonify(data)

api.add_resource(SentimentalAnalysis, '/')

if __name__ == '__main__':
    app.run(debug=True)