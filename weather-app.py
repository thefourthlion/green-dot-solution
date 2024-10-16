import requests
import json

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        main = weather_data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        weather_report = weather_data["weather"]
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {weather_report[0]['description']}") 
    else: 
        print("City Not Found!")
      
api_key = "Your_API_Key" 
city_name = input("Enter city name : ") 
get_weather(api_key, city_name)