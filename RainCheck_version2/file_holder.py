import json

class WeatherForecast:

    def __init__(self, filename="result.json"):
        self.filename = filename
        self.data = self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename,"r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def save(self, data):
        self.data.update(data)
        self.save_to_file()

    def load(self):
        return self.data

    def __setitem__(self, date, weather_info):
        self.data[date] = weather_info
        self.save_to_file()

    def __getitem__(self, date):
        return self.data.get(date, "Brak Danych")

    def __iter__(self):
        return iter(self.data)

    def exist(self, date):
        return date in self.data


