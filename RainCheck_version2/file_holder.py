import json


class WeatherForecast:

    def __init__(self, filename="result.json"):
        self.filename = filename
        self.data = self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def save(self, city, date, prediction):
        if city not in self.data:
            self.data[city] = {}
        self.data[city][date] = prediction
        self.save_to_file()

    def __getitem__(self, city):
        return self.data.get(city, {})

    def __setitem__(self, city, weather_info):
        if city not in self.data:
            self.data[city] = {}
        self.data[city].update(weather_info)
        self.save_to_file()

    def __iter__(self):
        for city, dates in self.data.items():
            for date in dates:
                yield city, date

    def items(self):
        for city, dates in self.data.items():
            for date, prediction in dates.items():
                yield (city, date), prediction

    def exist(self, city, date):
        return city in self.data and date in self.data[city]
