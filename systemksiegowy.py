Saldo = 100000
kontener = ["dodano 600000 zł do konta" , "odjęto 600000 zł z konta" , "Sprzedano Audi A7"]
autozbior = [
    {
        "marka": "Audi",
        "model": "A7",
        "rok": "2024",
        "kolor": "Czarny",
        "silnik": "Benzynowy",
        "przebieg": "12122 km",
        "ilość_sztuk": 10,
        "ilość_dostepnych_sztuk": 10,
        "cena": 600000,
    },
    {
        "marka": "Audi",
        "model": "A5",
        "rok": "2014",
        "kolor": "Biały",
        "silnik": "Diesel",
        "przebieg": "0 km",
        "ilość_sztuk": 3,
        "ilość_dostepnych_sztuk": 3,
        "cena": 70000,
    }
]
while True:
    print("Witam w programie do sprzedaży samochodów")
    wybor_użytkownika = input("Wybierz funkcje programu\n"
                              "1. Zmiana salda firmy\n"
                              "2. Sprzedaż samochodu\n"
                              "3. Dodanie samochodu do floty\n"
                              "4. Wyswietl stan konta firmy\n"
                              "5. Lista dostępnych pojazdów\n"
                              "6. Wyswietl dostepnośc konkretnego samochodu\n"
                              "7. Przeglad działań\n"
                              "8. Koniec\n"
                              "Wybór działania : ")
    if wybor_użytkownika == "1":
        kwota = float(input("Podaj kwotę o jaką chcesz zwiekszyć/zmniejszyć saldo: "))
        if Saldo + kwota <0:
            print("Brak środków na koncie !")
            kontener.append("Próba odjecia zbyt dużej kwoty")
        else:
            Saldo += kwota
            kontener.append(f"Zmiana salda o {kwota}")

    elif wybor_użytkownika == "2":
        marka = input("Podaj marke którą chcesz zakupić: ")
        model = input("Podaj model który chcesz zakupić: ")
        rok = input("Podaj rok wyprodukowania: ")
        znaleziono_samochod = False
        for samochod in autozbior:
            if samochod.get("marka") == marka and samochod.get("model") == model and samochod.get("rok") == rok:
                if samochod.get("ilość_dostepnych_sztuk") >= 1:
                    samochod["ilość_dostepnych_sztuk"] -=1
                    Saldo += samochod.get("cena")
                else:
                    print("Ten model został całkowicie wyprzedany, dostawa w trakcie")
                znaleziono_samochod = True
                break
        if not znaleziono_samochod:
            print("Nie znaleziono samochodu\n")

    elif wybor_użytkownika == "3":

    elif wybor_użytkownika == "4":
        print(Saldo)

    if wybor_użytkownika == "8":
        break
