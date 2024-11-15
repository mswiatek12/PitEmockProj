import logging
from fetch_module import use_fetch_module
from data_process import process_weather_data
import schedule
import time  # Needed to keep the scheduler running
import yaml
import os

# Set up logging for the whole app
log_dir = '../logs'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
file_handler = logging.FileHandler(f"{log_dir}/app.log")
logging.getLogger().addHandler(file_handler)


def run():
     
    # Fetching data
    logging.info("Starting data fetch...")
    use_fetch_module()

    # Processing data
    logging.info("Starting data processing...")
    process_weather_data()
    logging.info("Data processing complete.")


# scheduling every hour
schedule.every().hour.do(run)

if __name__ == '__main__':
    #initial run
    logging.info("Initial run")
    run()

    logging.info("Scheduler started, running `run()` every hour.")
    while True:
        schedule.run_pending()  #if task pending -> run
        time.sleep(1)
