import logging
import sys, os , traceback
import json

logger = logging.getLogger('Packt-Crawler')

formater = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
filehandlerInfo = logging.FileHandler('app.log')
filehandlerInfo.setFormatter(formater)
filehandlerInfo.setLevel(logging.INFO)

filehandlerDebug = logging.FileHandler('debug.log')
filehandlerDebug.setFormatter(formater)
filehandlerDebug.setLevel(logging.DEBUG)

filehandlerErr = logging.FileHandler('error.log')
filehandlerErr.setFormatter(formater)
filehandlerErr.setLevel(logging.ERROR)

logger.addHandler(filehandlerInfo)
logger.addHandler(filehandlerDebug)
logger.addHandler(filehandlerErr)

def log_success(msg):
    logger.addHandler(filehandlerInfo)
    logger.debug(msg)

def log_error(msg):
    logger.error(msg)

def log_debug(msg):
    logger.debug(msg)

def log_warn(msg):
    logger.warn(msg)

def log_dict(dict):
    for key, elem in dict.items():
        log_success('\t[{0}] {1}'.format(key, elem))
        print('\t[{0}] {1}'.format(key, elem))

def log_json(dicts):
    log_success('[json] {0}'.format(json.dumps(dicts, indent=2)))
    print('[json] {0}'.format(json.dumps(dicts, indent=2)))