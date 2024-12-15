import requests

def check_rain(latitude, logitude, searched_date):
    url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rain_sum = data.get("daily", {}).get("rain_sum", [None])[0]
        if rain_sum is None or rain_sum < 0:
            return "Nie wiem"
        elif rain_sum > 0.0:
            return "Będzie padać"
        else:
            return "Nie bedzie padać"
    else:
        return "Nie wiem"