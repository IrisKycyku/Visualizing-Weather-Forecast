import requests

API_KEY = "542d0e4d0ee5f7186ed126ce33b12a20"

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ =="__main__":
    get_data("London", 3)