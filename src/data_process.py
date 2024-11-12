import yaml
import cityWeather
import logging

#data should be already fetched

#logging configuration
logging.basicConfig(
    filename='../logs/app.log',
    filemode='a',  # append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # logging level
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

def process_weather_data(weather_data):
    city_weather_objects = {}

    for city_name, city_data in weather_data.items():
        try:
            city_weather = cityWeather(
                city_name=city_name,
                time=city_data['time'],
                temperature=city_data['temperature'],
                description=city_data['description'],
                feels_like=city_data['feels_like'],
                humidity=city_data['humidity'],
                pressure=city_data['pressure'],
                wind_speed=city_data['wind_speed']
            )
            city_weather_objects[city_name] = city_weather
        except KeyError as e:
            logging.error(f"Missing key {e} in weather data for {city_name}")

    return city_weather_objects

def main():
    # loading data from .yaml file
    weather_data_yaml = '../config/weather_data.yaml'
    weather_data = load_weather_data(weather_data_yaml)

    # putting .yaml data into cityWeather objects
    city_weather_objects = process_weather_data(weather_data)

    # logging actions
    for city, weather in city_weather_objects.items():
        logging.info(f"Processed weather data for {city}: {weather}")

if __name__ == '__main__':
    main()