import os

class Credentials():
    RAW_LOCAL_PATH = os.getcwd() + os.sep + 'data' + os.sep + 'RAW' + os.sep
    CURATED_LOCAL_PATH = os.getcwd() + os.sep + 'data' + os.sep + 'CURATED' + os.sep
    TEMPERATURES = r'temperatures.csv'
    TEMPERATURES_FILTRE = r'temperatures_filtre.csv'