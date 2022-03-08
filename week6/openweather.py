import my_notebooks.modules.api_keys as api_keys
import requests

url = "http://api.openweathermap.org/data/2.5/weather"
query = {
    "q": "Aarhus,dk",
    "mode": "json",
    "units": "metric",
    "appid": api_keys.OPENWEATHERMAP
}

r = requests.get(url, params=query)

print(r.json())
