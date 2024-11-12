from src.main import run
import config
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('../logs/app.log')
logging.getLogger().addHandler(console_handler)
logging.getLogger().addHandler(file_handler)

def runApp():
    logging.info("Running App from setup file.")
    run()

if __name__ == '__main__':
    runApp()