import urllib.request
import json

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            current = data['current_condition'][0]
            temp_c = float(current['temp_C'])
            # FEATURE ADDED: Convert to Fahrenheit
            temp_f = (temp_c * 9/5) + 32 
            
            desc = current['weatherDesc'][0]['value']
            humidity = current['humidity'] # FEATURE ADDED: Humidity tracking
            
            print(f"--- Weather Info for {city.capitalize()} ---")
            print(f"Temperature: {temp_c}°C ({temp_f:.1f}°F)")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {desc}")
    except Exception as e:
        print("Error fetching weather data. Please check the city name.")

if __name__ == "__main__":
    city_input = input("Enter city name: ")
    get_weather(city_input)
