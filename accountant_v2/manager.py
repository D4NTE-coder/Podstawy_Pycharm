import re
from file_hander import FileHandler
from colorama import Fore, Style, init

class Manager:
    def __init__(self, data_file, history_file):
        self.file_handler = FileHandler(data_file, history_file)
        self.data = self.file_handler.load_data()
        self.history = self.file_handler.load_history()
        self.saldo = self.data.get("saldo", 0)
        self.autozbior = self.data.get("autozbior", [])
        self.commands = {}


    def assign(self, command, function):
        self.commands[command] = function

    def execute(self, command, *args):
        if command in self.commands:
            return self.commands[command](*args)
        print(f"Nieznana komenda: {command}")

    def is_valid_name(self,marka):
        return bool(re.match("^[A-Za-z]+$", marka))

    def is_valid_year(self, year):
        return year.isdigit()

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
                if car["ilość_sztuk"] > 0:
                    car["ilość_sztuk"] -= 1
                    self.saldo += car["cena"]
                    self.history.append(f"Sprzedano {brand} {model} {year}")
                    print(f"Sprzedano {brand} {model} {year}")
                    if car["ilość_sztuk"] == 0:
                        self.autozbior.remove(car)
                    return
        print("Samochód niedostępny")

    def add_car(self, car_info):
        if not self.is_valid_name(car_info["marka"]):
            print("Błąd: Marka może zawierać tylko litery.")
            return

        if not self.is_valid_year(str(car_info["rok"])):
            print("Błąd: Rok powinien zawierać tylko cyfry.")
            return

        for car in self.autozbior:
            if car["marka"] == car_info["marka"] and car["model"] == car_info["model"] and car["rok"] == car_info["rok"] and car["cena"] == car_info["cena"]:
                car["ilość_sztuk"] += car_info["ilość_sztuk"]
                print(f"Zaktualizowano ilość sztuk {car_info['marka']} {car_info['model']} {car_info['rok']}. Nowa ilość: {car['ilość_sztuk']}")
                return

        self.autozbior.append(car_info)
        print(f"Dodano pojazd {car_info['marka']} {car_info['model']} {car_info['rok']}")

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
        self.file_handler.save_data(self.saldo, self.autozbior)
        self.file_handler.save_history(self.history)
