# weather_api.py - Get weather from internet
# Author: Jhosmar
# Date: 2026-04-19

import requests
import time

# API gratuita (no necesita clave para pruebas)
def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
# Author: Jhosmar
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "City not found"
    except:
        return "Error connecting to weather service"

def main():
    print("\n=== WEATHER API ===")
    print("Get current weather for any city")

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")

        if city.lower() == "exit":
            print("See you later!")
            break
# Author: Jhosmar

        print(f"\n🌤️ Fetching weather for {city}...")
        weather = get_weather(city)
        print(f"   {weather}")
        time.sleep(2)

if __name__ == "__main__":
    main()
# Author: Jhosmar
