import requests
from cacheFile import Cache
class WeatherAPI:
    
    def __init__(self, apiKey,url = None):
        self.key = apiKey
        self.url = url if url is not None else "https://api.openweathermap.org/data/2.5/weather"
    
    
    def getByCity(self,city):
        if not Cache.check(city):

            param = {
                "q" : city,
                "appid" : self.key
            }

            try :

                response = requests.get(self.url,params=param)
                Cache.update(city,response.json())
                return response.json()
                

            except requests.exceptions.ConnectionError:
                print("connection error")
            
            except requests.exceptions.ConnectTimeout:
                print("error connection timedout")
            
            except Exception as err:
                print(err)

            print("see logs file for more info about error")
            return None
        else:
            return Cache.check(city)
                