import urllib.request
import json

def get_weather(city):
    # Using a free, no-auth testing API endpoint
    url = f"https://wttr.in/{city}?format=j1"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            # Extract basic data
            current = data['current_condition'][0]
            temp = current['temp_C']
            desc = current['weatherDesc'][0]['value']
            
            print(f"--- Weather Info for {city.capitalize()} ---")
            print(f"Temperature: {temp}°C")
            print(f"Condition: {desc}")
    except Exception as e:
        print("Error fetching weather data. Please check the city name.")

if __name__ == "__main__":
    city_input = input("Enter city name: ")
    get_weather(city_input)