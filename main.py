import requests

def get_weather(city):
    api_key = '4d2646d3679bdf4bbf5c11db7e19cd9b' 
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    
    weather_data = response.json()
    return weather_data

def display_weather(weather_data):
    if weather_data['cod'] == 200:
        print(f"Weather in {weather_data['name']}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("City not found. Please check the input.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_info = get_weather(city_name)
    display_weather(weather_info)
