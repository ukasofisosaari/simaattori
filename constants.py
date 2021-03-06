"""constants.py

File for all the constants needed by different files.

@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""
import glob

#Database parameters
TEMPERATURE_DATABASE_NAME_DB = "simaattori_temperature.db"
TEMPERATURE_DATABASE_NAME_JSON = "simaattori_temperature.json"

DS18B20_BASE_DIR = '/sys/bus/w1/devices/'

#Timer, key is sensor id, value is time in seconds. How often temperature values are saved.
SENSOR_TIMINGS = {"28-000006564895": 3}
#Sensor information
SENSOR_ID_LOCATIONS = { "28-000006564895" : "Waterproof DS18B20 sensor" }



