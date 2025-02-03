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
        marka = str(input("Podaj markę: "))
        model = str(input("Podaj model: "))
        rok = int(input("Podaj rok: "))
        manager.execute("2", marka, model, rok)
    elif wybor == "3":
        car_info = {
            "marka": str(input("Marka: ")),
            "model": input("Model: "),
            "rok": int(input("Rok: ")),
            "cena": float(input("Cena: ")),
            "ilość_sztuk": int(input("Ilość sztuk: "))
        }
        manager.execute("3", car_info)
    elif wybor == "4":
        manager.execute("4")
    elif wybor == "5":
        manager.execute("5")
    elif wybor == "6":
        marka = str(input("Podaj markę: "))
        model = input("Podaj model: ")
        rok = int(input("Podaj rok: "))
        manager.execute("6", marka, model, rok)
    elif wybor == "7":
        manager.execute("7")

    manager.save_data()

    if wybor == "8":
        break
