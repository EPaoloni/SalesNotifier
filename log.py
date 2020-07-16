import logging
import json

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    with open('resources/config/config.json') as json_file:
        data = json.load(json_file)
        logPath = data['log-file-path']
    
    handler = logging.FileHandler(logPath, 'w')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger