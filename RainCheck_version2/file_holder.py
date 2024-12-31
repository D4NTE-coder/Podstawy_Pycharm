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

    def get_city_data(self, city):
        return self.data.get(city, {})

    def __getitem__(self, city):
        return self.data.get(city, "Brak danych")

    def __iter__(self):
        return iter(self.data)