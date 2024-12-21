import json
from services import (
    get_current_weather_json, 
    get_hourly_forcast_weather_json, 
    get_daily_forcast_weather_json, 
    get_monthly_frocast_weather_json
)
from datetime import datetime

def parse_current_weather(city_name):
    """
    Parse the current weather data for a given city.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        str: A formatted string containing the weather details.
    """
    data_str = get_current_weather_json(city_name)
    if data_str:
        data = json.loads(data_str)
        main = data['result']['weather'][0]['main']
        description = data['result']['weather'][0]['description']
        temp = data['result']['main']['temp']
        pressure = data['result']['main']['pressure']
        humidity = data['result']['main']['humidity']
        wind_speed = data['result']['wind']['speed']
        return f'Status: {main}\nDescription: {description}\nTemp: {temp}\nPressure: {pressure}\nHumidity: {humidity}\nWind Speed: {wind_speed}'
    else:
        return "No data available for the specified city."

def parse_hourly_weather(city_name):
    """
    Parse the hourly weather forecast for a given city.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        list: A list of formatted strings, each representing an hourly weather forecast.
    """
    data_str = get_hourly_forcast_weather_json(city_name)
    if data_str:
        data = json.loads(data_str)
        hours = data['result']['list'][:23]
        final_hour = []
        for hour in hours:
            final_hour.append(
                f"Status: {hour['weather'][0]['main']} "
                f"Temp: {hour['main']['temp']} "
                f"Pressure: {hour['main']['pressure']} "
                f"Humidity: {hour['main']['humidity']} "
                f"Wind Speed: {hour['wind']['speed']} "
                f"Time: {hour['dt_txt']}"
            )
        return final_hour
    else:
        return ["No data available for the specified city."]

def parse_daily_weather(city_name):
    """
    Parse the daily weather forecast for a given city.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        list: A list of formatted strings, each representing a daily weather forecast.
    """
    data_str = get_daily_forcast_weather_json(city_name)
    if data_str:
        data = json.loads(data_str)
        days = data['result']['list']
        final_days = []
        for day in days:
            date = datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d')
            final_days.append(f'date: {date} '
                f"Status: {day['weather'][0]['main']} "
                f"Temp: {day['temp']['day']} "
                f"Pressure: {day['pressure']} "
                f"Humidity: {day['humidity']} "
                f"Wind Speed: {day['speed']}"
            )
        return final_days
    else:
        return ["No data available for the specified city."]

def parse_monthly_weather(city_name):
    """
    Parse the monthly weather forecast for a given city.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        list: A list of formatted strings, each representing a monthly weather forecast.
    """
    data_str = get_monthly_frocast_weather_json(city_name)
    if data_str:
        data = json.loads(data_str)
        days = data['result']['list']
        final_days = []
        for day in days:
            date = datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d')
            final_days.append(
                f"Date: {date} "
                f"Status: {day['weather'][0]['main']} "
                f"Temp: {day['temp']['day']} "
                f"Pressure: {day['pressure']} "
                f"Humidity: {day['humidity']} "
                f"Wind Speed: {day['speed']}"
            )
        return final_days
    else:
        return ["No data available for the specified city."]
