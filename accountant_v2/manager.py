from file_hander import FileHandler

class Manager:
    def __init__(self, data_file, history_file):
        self.file_handler = FileHandler(data_file, history_file)
        self.data = self.file_handler.load_data_from_data_file()
        self.history = self.file_handler.load_data_from_history_file()
        self.saldo = self.data.get("saldo", 0)
        self.autozbior = self.data.get("autozbior", [])
        self.commands = {}

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
        found_car = None
        car_index = -1
        for index, car in enumerate(self.autozbior):
            if car.get("marka") == brand and car.get("model") == model and car.get("rok") == year:
                found_car = car
                car_index = index
                break
        if found_car is None:
            print("Samochód niedostępny")
            return
        if "ilość_sztuk" not in found_car:
            print(f"Błąd: Samochód {brand} {model} {year} nie ma klucza 'ilość_sztuk'.")
            return
        if "cena" not in found_car:
            print(f"Błąd: Samochód {brand} {model} {year} nie ma klucza 'cena'.")
            return
        if found_car["ilość_sztuk"] > 0:
            found_car["ilość_sztuk"] -= 1
            self.saldo += found_car["cena"]
            self.history.append(f"Sprzedano {brand} {model} {year}")
            print(f"Sprzedano {brand} {model} {year} za {found_car['cena']} zł")
            if found_car["ilość_sztuk"] == 0:
                del self.autozbior[car_index]
                print(f"{brand} {model} {year} został usunięty z autozbioru, ponieważ nie ma już dostępnych sztuk.")
            self.save_data()
        else:
            print(f"Brak dostępnych sztuk {brand} {model} {year}")

    def add_car(self, car_info):
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
        self.file_handler.save_data_to_data_file(self.saldo, self.autozbior)
        self.file_handler.save_data_to_history_file(self.history)
