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
                              "1.Zmiana salda firmy\n"
                              "2.Sprzedaż samochodu\n"
                              "3.Dodanie samochodu do floty\n"
                              "4.Wyswietl stan konta firmy\n"
                              "5.Lista dostępnych pojazdów\n"
                              "6.Wyswietl dostepnośc konkretnego samochodu\n"
                              "7.Przeglad działań\n"
                              "8.Koniec")
    if wybor_użytkownika == "8":
        break
