import requests
from speechrecognitionfunc import listen

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9)

def weather(command):
    if "what is the weather" in command:
        url = "https://api.openweathermap.org/data/2.5/weather?q=Accra&units=imperial&APPID=228f577dbcb14a0fac62acbbf17d040d"
        

        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        data = response.json()
        weather = data['weather'][0]['main']
        temp_fahrenheit = data['main']['temp']
        
        temp_celsius = fahrenheit_to_celsius(temp_fahrenheit)

        print(f"The weather is {weather}")
        print(f"The temperature is {temp_celsius}ºC")
        return f"The weather is {weather} and The temperature is {temp_celsius}ºC"
         







