import requests
import yaml
import time
import logging
import os
from dataFetcher import dataFetcher

os.makedirs('../logs', exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )


def use_fetch_module():
    config_file = '../config/config.yaml'

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    api_url = config['api_url']
    api_key = config['api_key']
    cities = config['cities']
    timeout = config['timeout']

    # creating dataFetcher obj and fetching
    fetcher_instance = dataFetcher(api_url, api_key, cities, timeout)
    fetcher_instance.fetch_all_cities_data()
