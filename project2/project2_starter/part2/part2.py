import json
import plotly.express as px
import pandas as pd
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%d %B")

def convert_f_to_c(temp_in_farenheit):
    temp_in_celsius = round((temp_in_farenheit - 32)*5/9,1)
    return temp_in_celsius

def open_json(forecast_file):
    with open(forecast_file) as json_file:
        forecast_data = json.load(json_file)
    return forecast_data
    
def create_dataframe(forecast_data):
    data_graph = {"Date":[],"Minimal":[],"Maximal":[],"Minimum_Feel":[],"MinFeelShade":[]}
    for item in forecast_data["DailyForecasts"]:
        date = convert_date(item["Date"])
        data_graph["Date"].append(date)
        min_temp = convert_f_to_c(item["Temperature"]["Minimum"]["Value"])
        data_graph["Minimal"].append(min_temp)
        max_temp = convert_f_to_c(item["Temperature"]["Maximum"]["Value"])
        data_graph["Maximal"].append(max_temp)
        max_temp = convert_f_to_c(item["RealFeelTemperature"]["Minimum"]["Value"])
        data_graph["Minimum_Feel"].append(max_temp)
        max_temp = convert_f_to_c(item["RealFeelTemperatureShade"]["Minimum"]["Value"])
        data_graph["MinFeelShade"].append(max_temp)
    #print(data_graph)
    df = pd.DataFrame(data_graph)
    # print(df)
    return data_graph

def create_graph1(df):
    first_day = df["Date"][0]
    last_day = df["Date"][-1]
    # using pandas dataframe
    fig = px.line(df, x="Date", y=["Maximal", "Minimal"]) 
    # can add a second line using a list for y
    # fig.add_scatter(x=df["Date"], y=df["Minimal"], name="Minimal")
    
    fig.update_traces(name = "Maximal", mode = "lines+markers")
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

def create_graph2(data_graph):
    first_day = data_graph["Date"][0]
    last_day = data_graph["Date"][-1]
    # without using pandas
    fig = px.bar(data_graph, x="Date", y="Minimum_Feel") 

    fig.update_traces(name = "Minimum Feel", showlegend = True)
    
    fig.add_scatter(x=data_graph["Date"], y=data_graph["Minimal"], name="Minimal", hoverinfo="x+y")
    fig.add_scatter(x=data_graph["Date"], y=data_graph["MinFeelShade"], name="Minimum Feel in the Shade", hoverinfo="x+y")
    #print(data_graph)
    fig.update_layout(
        title = f"How did you feel in the shade from {first_day} to {last_day} 2020",
        template="plotly_dark",
        xaxis_title = "Day",
        yaxis_title = f"Temperature in {DEGREE_SYMBOL}",
        legend_title="Temperature",
        font=dict(
            family="Arial",
            size=16,
        ),
        hoverlabel=dict(
        bgcolor="white", 
        font_size=16, 
        font_family="Rockwell"
    )
    )
    fig.show()

def draw_graph(forecast_file):
    forecast_data = open_json(forecast_file)
    data_graph = create_dataframe(forecast_data)
    create_graph1(data_graph)   
    create_graph2(data_graph)

draw_graph("data/forecast_5days_a.json")
# draw_graph("data/forecast_5days_b.json")
# draw_graph("data/forecast_10days.json")
