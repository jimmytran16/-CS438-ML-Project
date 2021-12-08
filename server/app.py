from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from services.loader import Loader

app = Flask(__name__)
CORS(app)
api = Api(app)

# endpoint for Sentimental Analysis
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
    
# endpoint for negative reasons analysis
class NegativesReasonsAnalysis(Resource):
    def __init__(self):
        self.loader = Loader()

    def get(self):
        data = {
            "virgin_america": self.loader.get_negative_reason_count_per_airline("Virgin America"),
            "united": self.loader.get_negative_reason_count_per_airline("United"),
            "southwest": self.loader.get_negative_reason_count_per_airline("Southwest"),
            "delta": self.loader.get_negative_reason_count_per_airline("Delta"),
            "us_airways": self.loader.get_negative_reason_count_per_airline("US Airways"),
            "american": self.loader.get_negative_reason_count_per_airline("American"),
        }

        return jsonify(data)

api.add_resource(SentimentalAnalysis, '/')
api.add_resource(NegativesReasonsAnalysis, '/negatives')

if __name__ == '__main__':
    app.run(debug=True)