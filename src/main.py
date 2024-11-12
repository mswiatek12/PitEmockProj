import logging
from fetch_module import use_fetch_module
from data_process import main as process_weather_data
import yaml
import os

# set up logging for the whole app
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('../logs/app.log')
logging.getLogger().addHandler(console_handler)
logging.getLogger().addHandler(file_handler)

def load_config():
    with open('../config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def run():
    print("Current working directory:", os.getcwd())
    #loading the config.yaml file (starter)
    config = load_config()

    # fetching data
    use_fetch_module()

    #processing data
    process_weather_data()

if __name__ == '__main__':
    run()