import requests
from city_coordinates import lat_long
from settings import BASE_URL

def get_current_weather_json(city_name):
    """
    Get the current weather data for a given city by its name.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        str: JSON response from the API if successful, None otherwise.
    """
    try:
        lat, lon = lat_long(city_name)
        action = f'&action=currentbylocation&lat={lat}&lon={lon}'
        response = requests.get(BASE_URL + action)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching current weather: {e}")
        return None

def get_hourly_forcast_weather_json(city_name):
    """
    Get the hourly weather forecast for a given city by its name.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        str: JSON response from the API if successful, None otherwise.
    """
    try:
        lat, lon = lat_long(city_name)
        action = f'&action=hourlybylocation&lat={lat}&lon={lon}'
        response = requests.get(BASE_URL + action)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching hourly forecast: {e}")
        return None

def get_daily_forcast_weather_json(city_name):
    """
    Get the daily weather forecast for a given city by its name.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        str: JSON response from the API if successful, None otherwise.
    """
    try:
        lat, lon = lat_long(city_name)
        action = f'&action=dailybylocation&lat={lat}&lon={lon}'
        response = requests.get(BASE_URL + action)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching daily forecast: {e}")
        return None

def get_monthly_frocast_weather_json(city_name):
    """
    Get the monthly weather forecast for a given city by its name.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        str: JSON response from the API if successful, None otherwise.
    """
    try:
        lat, lon = lat_long(city_name)
        action = f'&action=monthbylocation&lat={lat}&lon={lon}'
        response = requests.get(BASE_URL + action)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching monthly forecast: {e}")
        return None
