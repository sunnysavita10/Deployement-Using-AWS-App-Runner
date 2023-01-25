from app_logger import logger
from app_exception.exception import AppException
import pyowm
import sys


class WeatherData:
    def __init__(self):
        self.owmapikey='c8537154778558a3c9e30c03f18a1672'
        self.owm = pyowm.OWM(self.owmapikey)
    
    '''
    processing the request from dialogflow
    
    '''
    def processRequest(self,req):
        
        try:
            self.result = req.get("queryResult")
            self.parameters = self.result.get("parameters")
            self.city = self.parameters.get("city_name")
            
            self.observation = self.owm.weather_at_place(str(self.city))
            
            w = self.observation.get_weather()
            self.latlon_res = self.observation.get_location()
            
            self.lat = str(self.latlon_res.get_lat())
            self.lon = str(self.latlon_res.get_lon())

            self.wind_res = w.get_wind()
            self.wind_speed = str(self.wind_res.get('speed'))

            self.humidity = str(w.get_humidity())

            self.celsius_result = w.get_temperature('celsius')
            self.temp_min_celsius = str(self.celsius_result.get('temp_min'))
            self.temp_max_celsius = str(self.celsius_result.get('temp_max'))
            
            speech = "Today's the weather in " + str(self.city) + ":" + " , " +"Humidity : " + str(self.humidity) +" , " + "Wind Speed : " +str(self.wind_speed)+ " , " + "minimum temperature : " + str(self.temp_min_celsius) + " , " + "maximum temperature : " + str(self.temp_max_celsius)
        except Exception as e:
            raise AppException(e, sys)  from e  

        return {
            "fulfillmentText": speech,
            "displayText": speech
            }