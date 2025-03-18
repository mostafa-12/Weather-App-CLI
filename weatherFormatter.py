import colorama
from colorama import Fore, Style
from datetime import datetime
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
    @staticmethod


    def show_banner():
        colorama.init(autoreset=True)

        banner = f"""
        {Fore.CYAN}==========================================
        🌦️  {Fore.YELLOW}Weather CLI Application  {Fore.CYAN}🌦️
        =========================================={Style.RESET_ALL}
        {Fore.GREEN}
        █     █░ ███████  ▄▄▄       ██▓     ██▀███  
        ▓█░ █ ░█░ ██   ██ ▒████▄    ▓██▒    ▓██ ▒ ██▒
        ▒█░ █ ░█ ░██████ ▒██  ▀█▄  ▒██░    ▓██ ░▄█ ▒
        ░█░ █ ░█ ░██   ██░██▄▄▄▄██ ▒██░    ▒██▀▀█▄  
        ░░██▒██▓ ░██████  ▓█   ▓██▒░██████▒░██▓ ▒██▒
        ░ ▓░▒ ▒  ░░░░░░   ▒▒   ▓▒█░░ ▒░▓  ░░ ▒▓ ░▒▓░
        ▒ ░ ░    ░ ░ ░    ▒   ▒▒ ░░ ░ ▒  ░  ░▒ ░ ▒░
        ░   ░      ░      ░   ▒     ░ ░     ░░   ░ 
            ░      ░ ░        ░  ░    ░  ░   ░     
        {Style.RESET_ALL}

        {Fore.MAGENTA}Welcome to the Weather CLI! 🌍 {Style.RESET_ALL}
        This tool allows you to check weather information using an API.

        {Fore.YELLOW}📌 Available Commands:{Style.RESET_ALL}
        {Fore.GREEN}1️⃣ weather <city_name>{Style.RESET_ALL}  - Get weather information for a city
        {Fore.GREEN}2️⃣ clear-cache{Style.RESET_ALL}        - Clear stored cache
        {Fore.GREEN}3️⃣ exit{Style.RESET_ALL}               - Close the application

        """
        print(banner,end="")

    def get_api_key():
        while True:
            api_key = input(f"{Fore.YELLOW}🔑 Enter your OpenWeather API Key:{Style.RESET_ALL} ").strip()
            if api_key:
                return api_key
            print(f"{Fore.RED}⚠️ API Key is required! Please enter a valid key.{Style.RESET_ALL}")


