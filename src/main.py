import logging
from fetch_module import fetch_all_cities_data
from data_process import main as process_weather_data
import yaml

# set up logging for the whole app
logging.basicConfig(
    filename='../logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_config():
    with open('../config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def run():
    #loading the config.yaml file (starter)
    config = load_config()

    # fetching data
    fetch_all_cities_data(config)

    #processing data
    process_weather_data()

if __name__ == '__main__':
    run()