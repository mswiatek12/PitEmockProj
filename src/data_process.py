import yaml
from cityWeather import cityWeather
import logging
import datetime
#data should be already fetched

#logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


#yaml_file = '../config/weather_data.yaml'
def load_weather_data(yaml_file):
    try:
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except Exception as e:
        logging.error(f"Error reading YAML file: {e}")
        return {}

def deserialize(weather_data):
    city_weather_objects = {}

    for city_name, city_data in weather_data.items():
        try:
            # accessing nested dictionary values properly
            city_weather = cityWeather(
                city_name=city_name,
                time=city_data['dt'],
                temperature=city_data['main']['temp'],  # main -> temp
                description=city_data['weather'][0]['description'],
                feels_like=city_data['main']['feels_like'],
                humidity=city_data['main']['humidity'],
                pressure=city_data['main']['pressure'],
                wind_speed=city_data['wind']['speed']
            )

            city_weather_objects[city_name] = city_weather
        except KeyError as e:
            logging.error(f"Missing key {e} in weather data for {city_name}")

    return city_weather_objects

def process_weather_data():
    # loading data from .yaml file
    weather_data_yaml = '../config/weather_data.yaml'
    weather_data = load_weather_data(weather_data_yaml)

    # putting .yaml data into cityWeather objects
    city_weather_objects = deserialize(weather_data)

    # logging actions
    for city, weather in city_weather_objects.items():
        logging.info(f"Processed weather data for {city}: {weather}")