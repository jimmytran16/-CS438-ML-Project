import os.path
import pandas as pd

# Class that will parse and return data from excel
class Loader:
    def __init__(self):
        pass

    #  function to get the sentimental data for the graph
    def get_sentimentals_of_all_airlines(self):
        pos = 0
        neg = 0
        neut = 0

        df = self._parse_csv()

        for sent in df['airline_sentiment']:
            if sent == 'positive':
                pos += 1
            if sent == 'negative':
                neg += 1
            if sent == 'neutral':
                neut += 1

        return {
            "options": {
                "type": 'bar',
                "plugins": {
                    "title": {
                        "display": True,
                        "text": 'Airlines Sentimental Analysis'
                    }
                }
            },
            "data": {
                "labels": ['Positive', 'Neutral', 'Negative'],
                "datasets": [
                    {
                        "label": '# of Votes',
                        "data": [pos, neut, neg],
                        "backgroundColor": [
                            'rgba(40, 158, 81, 0.8)',
                            'rgba(106, 121, 112, 0.36)',
                            'rgba(179, 35, 78, 0.36)',
                        ],
                        "borderColor": [
                            'rgba(40, 158, 81, 0.8)',
                            'rgba(106, 121, 112, 0.36)',
                            'rgba(179, 35, 78, 0.36)',
                        ],
                        "borderWidth": 1,
                    },
                ],
            }
        }

    # function to get airline count data
    # will aggregrate the data set that is required for the chart
    def get_airline_count(self):
        df = self._parse_csv()

        airline_dict = {}
        data = []
        labels = []

        for airline in df['airline']:
            if airline not in airline_dict:
                airline_dict[airline] = 1
            else:
                airline_dict[airline] = airline_dict[airline] + 1

        for k, v in airline_dict.items():
            print(f"name: {k} count {v}")
            labels.append(k + ' Airlines')
            data.append(v)

        return {
            "data": {
                "labels": labels,
                "datasets": [
                    {
                        "label": 'Total',
                        "data": data,
                        "backgroundColor": 'rgba(255, 99, 132, 0.5)',
                    },
                ],
            },
            "options": {
                "responsive": True,
                "plugins": {
                    "legend": {
                        "position": 'top',
                    },
                    "title": {
                        "display": True,
                        "text": 'Airline Counts',
                    },
                },
            }
        }

        print(airline_dict)
    # function to parse and return the data within the csv file

    def _parse_csv(self):
        return pd.read_csv(os.path.dirname(__file__) + '/../Tweets.csv')


if __name__ == '__main__':

    loader = Loader()
    # print(loader.get_sentimentals_of_all_airlines())
    print(loader.get_airline_count())
