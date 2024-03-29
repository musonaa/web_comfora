import requests
def get_weather(city):
    API_KEY = "e10d7b63ce479b23474b88eade5541e6"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    weather = {
        "description": data['weather'][0]['description'],
        "temperature": round(data['main']['temp'] - 273.15, 2),
        "city": data['name'],
        "country": data['sys']['country']
    }
    return weather
