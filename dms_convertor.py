import re

def dms_to_decimal(dms_str):
    """
    Convert a DMS (degrees, minutes, seconds) format string to decimal format.

    Args:
        dms_str (str): A string representing coordinates in DMS format (e.g., "35° 41' 21.5\"").

    Returns:
        float: The converted coordinate in decimal format.

    Raises:
        ValueError: If the input string is not in the correct DMS format.
    """
    dms_regex = re.compile(r'(?P<degrees>\d+)[° ]+(?P<minutes>\d+)[\' ]+(?P<seconds>\d+(\.\d+)?)[\"]?')
    match = dms_regex.match(dms_str.strip())
    if not match:
        raise ValueError(f'Invalid DMS format: {dms_str}')
    
    degrees = int(match.group('degrees'))
    minutes = int(match.group('minutes'))
    seconds = float(match.group('seconds'))

    # Convert DMS to decimal
    decimal_degree = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degree


def convert_lat_long(lat_long_tuple):
    """
    Convert a tuple containing latitude and longitude in DMS format to decimal format.

    Args:
        lat_long_tuple (tuple): A tuple containing latitude and longitude in DMS format.

    Returns:
        tuple: A tuple with latitude and longitude in decimal format.
    """
    lat_dms, long_dms = lat_long_tuple

    lat_decimal = dms_to_decimal(lat_dms)
    long_decimal = dms_to_decimal(long_dms)

    return lat_decimal, long_decimal
