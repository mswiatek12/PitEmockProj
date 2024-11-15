import requests
import yaml
import time
#SCHEDULE FETCHING HOURLY(1)
import schedule

import logging
import os
import threading


log_dir = '../logs'
os.makedirs(log_dir, exist_ok=True)


# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


class dataFetcher:
    def __init__(self, api_url, api_key, cities, timeout):
        self.api_url = api_url
        self.api_key = api_key
        self.cities = cities
        self.timeout = timeout

    # preparing request & getting response
    def fetch_weather_data(self, lat, lon):
        try:
            response = requests.get(
                self.api_url,
                params={
                    'lat': lat,
                    'lon': lon,
                    'appid': self.api_key
                },
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logging.info(f"Error fetching data for coordinates ({lat}, {lon}): {e}")
            return None

    #freak bob callin
    def fetch_all_cities_data(self):
        logging.info("Starting concurrent data fetch...")
        weather_data = {}
        threads = []

        # function for thread
        def threadFetch(city):
            longitude = city['longitude']
            latitude = city['latitude']
            city_name = city['name']
            try:
                result = self.fetch_weather_data(latitude, longitude)
                if result:
                    weather_data[city_name] = result
            except Exception as exc:
                logging.error(f"Error fetching data for {city_name}: {exc}")

        # one city gets one thread 
        for city in self.cities:
            t = threading.Thread(target=threadFetch, args=(city,))
            threads.append(t)
            t.start()

        # making sure all threads are finished before writing into yaml file
        for t in threads:
            t.join()

        # finally dumping into yaml
        output_file = '../config/weather_data.yaml'
        with open(output_file, 'w') as file:
            yaml.dump(weather_data, file)
        logging.info(f"Weather data successfully saved to: {output_file}")
