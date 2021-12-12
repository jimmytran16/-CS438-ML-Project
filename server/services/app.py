from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

response =   {
	  "airlines": {
		  "data": {
			  "datasets": [{
				  "backgroundColor": "rgba(255, 99, 132, 0.5)",
				  "data": [504, 3822, 2420, 2222, 2913, 2759],
				  "label": "Total"
			  }],
			  "labels": ["Virgin America Airlines", "United Airlines", "Southwest Airlines", "Delta Airlines", "US Airways Airlines", "American Airlines"]
		  },
		  "options": {
			  "maintainAspectRatio": False,
			  "plugins": {
				  "legend": {
					  "position": "top"
				  },
				  "title": {
					  "display": True,
					  "text": "Airline Counts"
				  }
			  },
			  "responsive": True
		  }
	  },
	  "sentimental": {
		  "data": {
			  "datasets": [{
				  "backgroundColor": ["rgba(40, 158, 81, 0.8)", "rgba(106, 121, 112, 0.36)", "rgba(179, 35, 78, 0.36)"],
				  "borderColor": ["rgba(40, 158, 81, 0.8)", "rgba(106, 121, 112, 0.36)", "rgba(179, 35, 78, 0.36)"],
				  "borderWidth": 1,
				  "data": [2363, 3099, 9178],
				  "label": "Total"
			  }],
			  "labels": ["Positive", "Neutral", "Negative"]
		  },
		  "optionsBar": {
			  "maintainAspectRatio": False,
			  "plugins": {
				  "title": {
					  "display": True,
					  "text": "Airlines Sentimental Analysis"
				  }
			  },
			  "responsive": True
		  },
		  "optionsDoughnut": {
			  "plugins": {
				  "title": {
					  "display": True,
					  "text": "Airlines Sentimental Analysis"
				  }
			  }
		  }
	  },
	  "negative": {
		  "data": {
			  "datasets": [{
				  "backgroundColor": ["rgba(40, 158, 81, 0.8)", "rgba(106, 121, 112, 0.36)", "rgba(179, 35, 78, 0.36)"],
				  "borderColor": ["rgba(40, 158, 81, 0.8)", "rgba(106, 121, 112, 0.36)", "rgba(179, 35, 78, 0.36)"],
				  "borderWidth": 1,
				  "data": [69, 69, 100],
				  "label": "Total"
			  }],
			  "labels": ["ulala", "ulalala", "ulalalalal"]
		  },
		  "optionsBar": {
			  "maintainAspectRatio": False,
			  "plugins": {
				  "title": {
					  "display": True,
					  "text": "Airlines Sentimental Analysis"
				  }
			  },
			  "responsive": True
		  },
		  "optionsDoughnut": {
			  "plugins": {
				  "title": {
					  "display": True,
					  "text": "Airlines Sentimental Analysis"
				  }
			  }
		  }
	  },
      }

  

@app.route('/test/blah')

def hello_world():
    return response
 
if __name__ == '__main__':
    app.run()