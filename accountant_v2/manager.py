from file_hander import FileHandler
from colorama import Fore, Style, init


class Manager:
    def __init__(self, data_file, history_file):
        self.file_handler = FileHandler(data_file, history_file)
        self.data = self.file_handler.load_data_from_data_file()
        self.history = self.file_handler.load_data_from_history_file()
        self.saldo = self.data.get("saldo", 0)
        self.autozbior = self.data.get("autozbior", [])
        self.commands = {}
        init(autoreset=True)

    def assign(self, command, function):
        self.commands[command] = function

    def execute(self, command, *args):
        if command in self.commands:
            return self.commands[command](*args)
        print(f"Nieznana komenda: {command}")

    def change_balance(self, amount):
        if self.saldo + amount < 0:
            print(f"Brak środków na koncie!")
            self.history.append("Próba odjęcia zbyt dużej kwoty")
        else:
            self.saldo += amount
            self.history.append(f"Zmiana salda o {amount}")

    def sell_car(self, brand, model, year):
        for car in self.autozbior:
            if car["marka"] == brand and car["model"] == model and car["rok"] == year:
                if car["ilość_dostepnych_sztuk"] > 0:
                    car["ilość_dostepnych_sztuk"] -= 1
                    self.saldo += car["cena"]
                    self.history.append(f"Sprzedano {brand} {model} {year}")
                    print(f"Sprzedano {brand} {model} {year}")
                    return
        print("Samochód niedostępny")

    def add_car(self, car_info):
        self.autozbior.append(car_info)
        self.saldo -= car_info["cena"] * car_info["ilość_sztuk"]
        self.history.append(f"Dodano pojazd {car_info['marka']} {car_info['model']} {car_info['rok']}")

    def display_balance(self):
        print(f"Saldo: {self.saldo}")

    def list_cars(self):
        for car in self.autozbior:
            print(car)

    def check_car_availability(self, brand, model, year):
        for car in self.autozbior:
            if car["marka"] == brand and car["model"] == model and car["rok"] == year:
                print(car)
                return
        print("Samochód niedostępny")

    def review_history(self):
        for entry in self.history:
            print(entry)

    def save_data(self):
        self.file_handler.save_data_to_data_file(self.saldo, self.autozbior)
        self.file_handler.save_data_to_history_file(self.history)
