import json
from dms_convertor import convert_lat_long

def get_lat_and_long_city(city_name):
    """
    Get the latitude and longitude of a city from a .json file.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        tuple: Latitude and longitude of the city in DMS format.

    Raises:
        FileNotFoundError: If the cities.json file cannot be found.
        KeyError: If the city is not present in the data.
    """
    try:
        with open('Cities.json', 'r', encoding='utf-8') as f:
            # file reference: https://gist.github.com/alirezanet/0bbfb2921e421f8acb46244e0b5a8f8a#file-iran96-97-json
            data = json.load(f)
            for city in data:
                if city['city'] == city_name:
                    return city['latitude'], city['longitude']
            raise KeyError(f"City '{city_name}' not found in the data.")
    except FileNotFoundError:
        raise FileNotFoundError("Cities.json file not found. Make sure the file exists in the directory.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON. Ensure the Cities.json file is properly formatted.")

def lat_long(city_name):
    """
    Convert the latitude and longitude of a city to decimal format.

    Args:
        city_name (str): The name of the city in Persian.

    Returns:
        tuple: Latitude and longitude in decimal format.
    """
    return convert_lat_long(get_lat_and_long_city(city_name))
