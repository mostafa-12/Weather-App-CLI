import requests

class WeatherAPI:
    
    def __init__(self, apiKey,url = None):
        self.key = apiKey
        self.url = url if url is not None else "https://api.openweathermap.org/data/2.5/weather"
    
    
    def getByCity(self,city):
        
        param = {
            "q" : city,
            "appid" : self.key
        }

        try :

            response = requests.get(self.url,params=param)
            return response.json()
        
        except requests.exceptions.ConnectionError:
            print("connection error")
        
        except requests.exceptions.ConnectTimeout:
            print("error connection timedout")
        
        except Exception as err:
            print(err)

        print("see logs file for more info about error")
        return None
            