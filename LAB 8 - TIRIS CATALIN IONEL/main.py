import requests
API_KEY = "57f38a975fe2d30f45d94008584d29c7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Introdu numele orasului: ")
request_url = f"{BASE_URL}?appid={API_KEY}6q={city}6units=metric"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    print(data)
    vreme=data['weather'][0]['description']
    temperature = round(data["main"]["temp"], 2)
    print("Vremea: ", vreme)
    print("Temperatura", temperature)
else:
    print("An intampinat o eroare")