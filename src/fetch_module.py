import requests
import yaml
import time
import schedule
import logging
import os

#fetching data ;)

os.makedirs('../logs', exist_ok=True)

#logging configuration
logging.basicConfig(
    filename='../logs/app.log',
    filemode='a',  # append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # logging level
)

config_file = '../config/config.yaml'

with open(config_file, 'r') as file:
    config = yaml.safe_load(file)

api_url = config['api_url']
api_key = config['api_key']
cities = config['cities']
timeout = config ['timeout']

def fetch_weather_data(lat, lon, api_url, api_key, timeout):
    try:
        response = requests.get(
            api_url,
            params={
                'lat': lat,
                'lon': lon,
                'appid': api_key
            },
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.info(f"Error fetching data for coordinates ({lat}, {lon}): {e}")
        return None

def fetch_all_cities_data():

    logging.info("Starting hourly data fetch...")
    weather_data = {}

    for city in cities:
        city_name = city['name']
        lat = city['latitude']
        lon = city['longitude']
        logging.info(f"Fetching data for {city_name}...")
        city_weather = fetch_weather_data(lat, lon, api_url, api_key, timeout)
        if city_weather:
            weather_data[city_name] = city_weather
        time.sleep(1)  #avoid overloading server, we got time

    #dumping data into .yaml file
    output_file = '../config/weather_data.yaml'
    with open(output_file, 'w') as file:
        yaml.dump(weather_data, file)
    logging.info(f"Weather data successfully saved to: {output_file}")

#one request per hour
schedule.every(1).hour.do(fetch_all_cities_data)

#looping schedule
while True:
    try:
        schedule.run_pending()
        time.sleep(60)  # check every minute
    except Exception as e:
        logging.error(f"Error during scheduled task: {e}")
        time.sleep(60)  # wait before retrying