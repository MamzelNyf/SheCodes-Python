import json
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius
    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_celsius = round((temp_in_farenheit - 32)*5/9,1)
    return temp_in_celsius
    

def calculate_mean(total, num_items):
    """Calculates the mean.
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = float(round((total / num_items),1))
    return mean

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.
    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    # import os
    # dir_name = os.path.dirname(os.path.abspath(__file__))
    # json_file_path = os.path.join(dir_name,forecast_file)
    with open(forecast_file) as json_file:
        forecast_data = json.load(json_file)

    # Create a list to save dates and temperatures for the period
    temperature_average = t = [[],[],[]]
    output_daily = []
    for items in forecast_data["DailyForecasts"]:
        converted_date = convert_date(items["Date"])
        t[0].append(converted_date)
        output_daily.append("-------- " + converted_date + " --------")

        min_temp_per_date = convert_f_to_c(items["Temperature"]["Minimum"]["Value"])
        t[1].append(min_temp_per_date)
        output_daily.append("Minimum Temperature: " + format_temperature(str(min_temp_per_date)))
        
        max_temp_per_date = convert_f_to_c(items["Temperature"]["Maximum"]["Value"])
        t[2].append(max_temp_per_date)
        output_daily.append("Maximum Temperature: " + format_temperature(str(max_temp_per_date)))
    
        # Append data from a loop in a list to be able to return it formatted
        output_daily.append(f"""Daytime: {items["Day"]["LongPhrase"]}""")
        output_daily.append(f"""    Chance of rain:  {items["Day"]["RainProbability"]}%""")
        output_daily.append(f"""Nighttime: {items["Night"]["LongPhrase"]}""")
        output_daily.append(f"""    Chance of rain:  {items["Night"]["RainProbability"]}%\n""")
    # print(t)
    # print(output_daily)
    
    # Save min and max temperature for the period, save index for corresponding date
    # min_temp_for_period = min(t[1])
    # max_temp_for_period = max(t[2])
    min_temp_day = t[0][t[1].index(min(t[1]))]
    max_temp_day = t[0][t[2].index(max(t[2]))]
    # print(f"{min_temp_for_period}, {max_temp_for_period}, {min_temp_day}, {max_temp_day}")

    # Calculate mean of temperature for the period
    #number_days = len(t[0])
    min_temp_mean = calculate_mean(sum(t[1]), len(t[0]))
    max_temp_mean = calculate_mean(sum(t[2]), len(t[0]))
    # print(f"{number_days}, {min_temp_mean}, {max_temp_mean}")

    # save a formatted text in a variable to be able to return it
    output_header = f"""{len(t[0])} Day Overview
    The lowest temperature will be {format_temperature(min(t[1]))}, and will occur on {min_temp_day}.
    The highest temperature will be {format_temperature(max(t[2]))}, and will occur on {max_temp_day}.
    The average low this week is {format_temperature(min_temp_mean)}.
    The average high this week is {format_temperature(max_temp_mean)}.\n
"""
    # Join all items in a list into a string, using a character as separator:
    return output_header + "\n".join(output_daily) + "\n"

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_b.json"))

