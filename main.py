from parsing import *

def runner():
    try:
        city_name = input('Please enter the city name in Persian:\n')
        forecast_type = input('Enter type of forecast (current, hourly, daily, month):\n').lower()

        if forecast_type == 'current':
            result = parse_current_weather(city_name)
            print(result)
        elif forecast_type == 'hourly':
            result = parse_hourly_weather(city_name)
            for i in result:
                print(i)
        elif forecast_type == 'daily':
            result = parse_daily_weather(city_name)
            for i in result:
                print(i)
        elif forecast_type == 'month':
            result = parse_monthly_weather(city_name)
            for i in result:
                print(i)
        else:
            print("Invalid forecast type. Please enter one of: current, hourly, daily, month.")
    except KeyError:
        print(f"City '{city_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    while True:
        runner()
