import json
import plotly.express as px
#import pandas as pd
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%d %B")

def convert_f_to_c(temp_in_farenheit):
    temp_in_celsius = round((temp_in_farenheit - 32)*5/9,1)
    return temp_in_celsius
    

def create_graph1(forecast_file):
    with open(forecast_file) as json_file:
        forecast_data = json.load(json_file)
    
    data_graph = {"Date":[],"Minimal":[],"Maximal":[]}
    for item in forecast_data["DailyForecasts"]:
        date = convert_date(item["Date"])
        data_graph["Date"].append(date)
        min_temp = convert_f_to_c(item["Temperature"]["Minimum"]["Value"])
        data_graph["Minimal"].append(min_temp)
        max_temp = convert_f_to_c(item["Temperature"]["Maximum"]["Value"])
        data_graph["Maximal"].append(max_temp)
    #print(data_graph)

    #df = pd.DataFrame(data_graph)
    # print(df)
    first_day = data_graph["Date"][0]
    last_day = data_graph["Date"][-1]
    fig = px.line(data_graph, x="Date", y="Maximal") 
    fig.update_traces(name = "Maximal", showlegend = True,
                    mode = "lines+markers")
    fig.add_scatter(x=data_graph["Date"], y=data_graph["Minimal"], name="Minimal" )
    fig.update_layout(
        title = f"Temperatures maximal and minimal from {first_day} to {last_day} 2020",
        template="gridon",
        xaxis_title = "Day",
        yaxis_title = f"Temperature in {DEGREE_SYMBOL}",
        legend_title="Temperature",
        font=dict(
            family="Courier New, monospace",
            size=16,
    )
)
    fig.show()

create_graph1("data/forecast_5days_b.json")


