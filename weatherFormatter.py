from colorama import Fore, Style
from datetime import datetime
import weatherAPI
class WeatherFormatter:
    @staticmethod
    def displayWeather(weather):
        output = (f"{Fore.CYAN}🏙️  Weather in {weather['name']}, {weather['sys']['country']}{Style.RESET_ALL}\n"
            f"{Fore.YELLOW}🌡️  Temperature: {weather['main']['temp']} (Feels like: {weather['main']['feels_like']}){Style.RESET_ALL}\n"
            f"{Fore.BLUE}💧 Humidity: {weather['main']['humidity']}{Style.RESET_ALL}\n"
            f"{Fore.GREEN}☁️  Weather Condition: {weather['weather'][0]['description']}{Style.RESET_ALL}\n"
            f"{Fore.MAGENTA}💨 Wind Speed: {weather['wind']['speed']} - Direction: {weather['wind']['deg']}deg{Style.RESET_ALL}\n"
            f"{Fore.RED}🌅 Sunrise: {datetime.fromtimestamp(weather['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')} | 🌇 Sunset: {datetime.fromtimestamp(weather['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}"
                  
                  )
        return output
    

