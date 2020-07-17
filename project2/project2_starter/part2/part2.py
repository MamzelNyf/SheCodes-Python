import json
import plotly.express as px

def graph(forecast_file):
    with open(forecast_file) as json_file:
        forecast_data = json.load(json_file)

        
if __name__ == "__main__":
    print(graph("data/forecast_5days_b.json"))