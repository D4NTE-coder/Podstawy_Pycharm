from colorama import Fore, Style, init
from file_hander import FileHandler

file_handler = FileHandler(data_file="dane_salonu.json", history_file="historia.json")
init(autoreset=True)

data = file_handler.load_data_from_data_file()
kontener = file_handler.load_data_from_history_file()

Saldo = data.get("saldo")
separator = "-" * 100
autozbior = data.get("autozbior")
while True:
    print("Witam w programie do sprzedaży samochodów")
    wybor_użytkownika = input(
        "Wybierz funkcje programu\n"
        "1. Zmiana salda firmy\n"
        "2. Sprzedaż samochodu\n"
        "3. Dodanie samochodu do floty\n"
        "4. Wyswietl stan konta firmy\n"
        "5. Lista dostępnych pojazdów\n"
        "6. Wyswietl dostepnośc konkretnego samochodu\n"
        "7. Przeglad działań\n"
        "8. Koniec\n"
        "Wybór działania : "
    )
    if wybor_użytkownika == "1":
        kwota = float(input("Podaj kwotę o jaką chcesz zwiekszyć/zmniejszyć saldo: "))
        if Saldo + kwota < 0:
            print(f"Brak środków na koncie !\n{separator}")
            kontener.append("Próba odjecia zbyt dużej kwoty ")
        else:
            Saldo += kwota
            kontener.append(f"Zmiana salda o {kwota} \n{separator}")

    elif wybor_użytkownika == "2":
        marka = input("Podaj marke którą chcesz sprzedać: ")
        model = input("Podaj model który chcesz sprzedać: ")
        rok = input("Podaj rok wyprodukowania: ")
        znaleziono_samochod = False
        for samochod in autozbior:
            if (
                samochod.get("marka") == marka
                and samochod.get("model") == model
                and samochod.get("rok") == rok
            ):
                if samochod.get("ilość_dostepnych_sztuk") >= 1:
                    samochod["ilość_dostepnych_sztuk"] -= 1
                    Saldo += samochod.get("cena")
                    print(
                        f"Sprzedałeś samochód {Fore.YELLOW}{marka} {model} {rok}{Style.RESET_ALL}\n{separator}"
                    )
                    kontener.append(
                        f"Sprzedano samochód {Fore.YELLOW}{marka} {model} {rok}{Style.RESET_ALL}"
                    )
                else:
                    print(
                        f"{Fore.RED}Ten model został całkowicie wyprzedany, dostawa w trakcie{Style.RESET_ALL} {separator}"
                    )
                znaleziono_samochod = True
                break
        if not znaleziono_samochod:
            print(f"{Fore.RED}Nie znaleziono samochodu{Style.RESET_ALL}\n {separator}")

    elif wybor_użytkownika == "3":
        marka = input("Podaj marke którą chcesz zakupić: ")
        model = input("Podaj model który chcesz zakupić: ")
        rok = int(input("Podaj rok wyprodukowania: "))
        kolor = input("Podaj kolor który chcesz zakupić:")
        silnik = input("Podaj silnik jaki ma pojazd: ")
        try:
            przebieg = int(input("Podaj przebieg jaki posiada pojazd: "))
            ilosc_sztuk = int(input("Podaj ilość sztuk która chcesz zakupić: "))
            cena_zakup = float(input("Podaj kwotę za którą zakupiony został pojazd: "))
            cena_sprzedarz = float(input("Podaj kwotę za jaką wystawiasz pojazd: "))
            if ilosc_sztuk <= 0 or cena_zakup <= 0:
                print(
                    f"{Fore.RED} Zakup nie może zostać zrealizowany ilość sztuk i cena muszą być wieksze od 0{Style.RESET_ALL}"
                )
                continue
        except ValueError:
            print(f"{Fore.RED}Podano nie prawidłowe dane{Style.RESET_ALL} {separator}")
            continue
        if ilosc_sztuk * cena_zakup > Saldo:
            print(
                f"{Fore.RED}Nie posiadasz wystarczająch środków zeby kupić pojazd:{Style.RESET_ALL} {separator}"
            )
            continue
        autozbior.append(
            {
                "marka": marka,
                "model": model,
                "rok": rok,
                "kolor": kolor,
                "silnik": silnik,
                "przebieg": przebieg,
                "ilość_sztuk": ilosc_sztuk,
                "ilość_dostepnych_sztuk": ilosc_sztuk,
                "cena": cena_sprzedarz,
            }
        )
        Saldo -= ilosc_sztuk * cena_zakup
        print(f"Dodano pojazd {Fore.YELLOW}{marka} {model} {rok}{Style.RESET_ALL}")
        kontener.append(f"Dodano pojazd {marka} {model} {rok}")

    elif wybor_użytkownika == "4":
        print(f"{Fore.YELLOW}{Saldo}{Style.RESET_ALL}\n{separator}")
        kontener.append(f"Sprawdzono stan konta firmy - {Saldo} zł")

    elif wybor_użytkownika == "5":
        for samochod in autozbior:
            print(separator)
            for klucz, wartosc in samochod.items():
                print(f"{klucz}: {wartosc}")
            print(separator)
        kontener.append(f"Wyświetlono listę dostępnych pojazdów")

    elif wybor_użytkownika == "6":
        marka = input("Podaj markę samochodu: ")
        model = input("Podaj model samochodu: ")
        rok = input("Podaj rok produkcji: ")
        for samochod in autozbior:
            if (
                samochod["marka"] == marka
                and samochod["model"] == model
                and samochod["rok"] == rok
            ):
                print(f"{Fore.YELLOW}{samochod}{Style.RESET_ALL}")
        else:
            print(f"Nie znaleziono samochodu.{separator}")
        kontener.append(
            f"Przeszukano baze w poszukiwaniu samochodu {marka} {model} {rok}"
        )

    elif wybor_użytkownika == "7":
        try:
            od = input(
                "Podaj indeks początkowy(lub zostaw puste pole od zakresu początkowego"
            )
            do = input(
                "Podaj indeks końcowy(lub zostaw puste pole od zakresu końcowego"
            )

            od = int(od) if od else 0
            do = int(do) if do else len(kontener)

            if od < 0 or do > len(kontener) or od >= do:
                print(
                    f"{Fore.RED}Nieprawidłowy zakres! Liczba dostępnych operacji:{Style.RESET_ALL} {len(kontener)} {separator}"
                )
            else:
                print(f"Przegląd działan {od} do {do}: ")
                for i in range(od, do):
                    print(f"{i +1}. {kontener[i]}")
        except ValueError:
            print(
                f"{Fore.RED}Podano nieprawidłowe wartości indeksów.{Style.RESET_ALL} "
            )
        kontener.append(f"Sprawdzono historię działań od {od} do {do}")

    file_handler.save_data_to_data_file(balance=Saldo, car_collection=autozbior)
    file_handler.save_data_to_history_file(history=kontener)

    if wybor_użytkownika == "8":
        break


