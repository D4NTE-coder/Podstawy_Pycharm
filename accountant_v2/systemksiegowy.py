from manager import Manager

manager = Manager("dane_salonu.json", "historia.json")

manager.assign("1", manager.change_balance)
manager.assign("2", manager.sell_car)
manager.assign("3", manager.add_car)
manager.assign("4", manager.display_balance)
manager.assign("5", manager.list_cars)
manager.assign("6", manager.check_car_availability)
manager.assign("7", manager.review_history)

while True:
    wybor = input(
        "Wybierz funkcję programu\n"
        "1. Zmiana salda firmy\n"
        "2. Sprzedaż samochodu\n"
        "3. Dodanie samochodu\n"
        "4. Wyświetl saldo\n"
        "5. Lista pojazdów\n"
        "6. Sprawdź dostępność\n"
        "7. Historia działań\n"
        "8. Koniec\nWybór: ")

    if wybor == "1":
        kwota = float(input("Podaj kwotę: "))
        manager.execute("1", kwota)
    elif wybor == "2":
        marka = input("Podaj markę: ")
        while not manager.is_valid_name(marka):
            print("Błąd: Marka może zawierać tylko litery.")
            marka = input("Podaj markę: ")
        model = input("Podaj model: ")
        rok = input("Podaj rok: ")
        while not manager.is_valid_year(rok):
            print("Błąd: Rok powinien zawierać tylko cyfry.")
            rok = input("Podaj rok: ")
        manager.execute("2", marka, model, rok)
    elif wybor == "3":

        while True:
            marka = input("Marka: ")
            if not marka.isalpha():
                print("Marka musi zawierać tylko litery!")
                continue
            break

        model = input("Model: ")

        while True:
            try:
                rok = int(input("Rok: "))
                if rok < 1900 or rok > 2023:
                    print("Rok musi być pomiędzy 1900 a 2023!")
                    continue
                break
            except ValueError:
                print("Rok musi zawierać tylko cyfry!")
                continue

        cena = float(input("Cena: "))
        ilosc_sztuk = int(input("Ilość sztuk: "))

        car_info = {
            "marka": marka,
            "model": model,
            "rok": rok,
            "cena": cena,
            "ilość_sztuk": ilosc_sztuk
        }

        manager.execute("3", car_info)
    elif wybor in ["4", "5", "7"]:
        manager.execute(wybor)
    elif wybor == "6":
        marka = input("Podaj markę: ")
        model = input("Podaj model: ")
        rok = int(input("Podaj rok: "))
        manager.execute("6", marka, model, rok)

    manager.save_data()

    if wybor == "8":
        break
