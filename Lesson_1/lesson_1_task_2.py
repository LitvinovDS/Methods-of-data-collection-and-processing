import requests
import json


def get_weather(city_name, api_key):
    req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
    print(json.dumps(req.json(), indent=4))


my_api_key = '8084a93013cedb170332ec3772d35b9e'
current_city = input('Введите название города: ')
get_weather('Moscow', my_api_key)
