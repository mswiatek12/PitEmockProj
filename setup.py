import main
import config
import logging

logging.basicConfig(
    filename='../logs/app.log',
    filemode='a',  # append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO  # logging level
)

def runApp():
    logging.info("Running App from setup file.")
    main.run()

if __name__ == '__main__':
    runApp()