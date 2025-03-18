import weatherAPI
import weatherFormatter
import cacheFile
import os
from colorama import Fore
import time

def main():
    API = weatherFormatter.WeatherFormatter.get_api_key()
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        weatherFormatter.WeatherFormatter.show_banner()

        choice = input(" : ")

        if choice == "1":
            print(Fore.CYAN,"enter city : ",Fore.RESET,end="")
            
            city= input() 

            weather = weatherAPI.WeatherAPI(API)

            cityWeather = weather.getByCity(city)

                        
            formatted_Weather = weatherFormatter.WeatherFormatter.displayWeather(cityWeather)

            print(formatted_Weather)
            print('\n\n')
            input("🔹 Press Enter to continue...")
        elif choice == "2":

            cacheFile.Cache.clearCache()
            print(Fore.GREEN,"cache cleared ✅",Fore.RESET)
        
        elif choice == "3":
        
            print(Fore.GREEN, "see you later pro 👋")
            exit()
        
        else:
        
            print(Fore.RED,"Invalid input, please try again after 5 sec ",Fore.RESET)
            time.sleep(5)
            continue
        
        print(Fore.YELLOW,"wait 3 sec to do other process 😁",Fore.RESET)



if __name__ == "__main__":
    main()