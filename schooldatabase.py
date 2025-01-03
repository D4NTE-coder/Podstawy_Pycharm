from colorama import Fore, Style, init

init(autoreset=True)


class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} z klasy {self.klasa}"


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = []

    def dodaj_klase(self, klasa):
        self.klasy.append(klasa)

    def __repr__(self):
        klasy_str = ", ".join(self.klasy) if self.klasy else "Brak klas"
        return f"{self.imie} {self.nazwisko} jest nauczycielem {self.przedmiot} i prowadzi klasy: {klasy_str}"


class Wychowawca:
    def __init__(self, imie, nazwisko, prowadzona_klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.prowadzona_klasa = prowadzona_klasa

    def __repr__(self):
        return (
            f"{self.imie} {self.nazwisko} jest wychowawcą klasy {self.prowadzona_klasa}"
        )


def wyszukiwanie_uczniów_w_klasie(nazwa_klasy):
    uczniowie_klasa = [uczen for uczen in uczniowie if uczen.klasa == nazwa_klasy]

    wychowawca_klasy = next(
        (
            wychowawca
            for wychowawca in wychowawcy
            if wychowawca.prowadzona_klasa == nazwa_klasy
        ),
        None,
    )
    return uczniowie_klasa, wychowawca_klasy


def zarzadzaj_klasa():
    nazwa_klasy = input("Podaj Klase którą chcesz sprawdzić")
    uczniowie_klasa, wychowawca_klasy = wyszukiwanie_uczniów_w_klasie(nazwa_klasy)
    print(f"\nUczniowie w klasie {nazwa_klasy}:")
    for uczen in uczniowie_klasa:
        print(f" - {Fore.YELLOW}{uczen}{Style.RESET_ALL}")
    if wychowawca_klasy:
        print(
            f"Wychowawcą klasy {Fore.YELLOW} {nazwa_klasy} {Style.RESET_ALL} jest : {Fore.YELLOW}{wychowawca_klasy}"
        )
    else:
        print(f"{Fore.RED}Ta klasa nie ma obecnie wychowawcy{Style.RESET_ALL}")


def zarzadzaj_uczniem():
    imie = input("Podaj imie ucznia: ")
    nazwisko = input("Podaj nazwisko ucznia: ")
    uczen = next(
        (
            uczen
            for uczen in uczniowie
            if uczen.imie == imie and uczen.nazwisko == nazwisko
        ),
        None,
    )
    if uczen:
        print(
            f"Lekcje ucznia {Fore.YELLOW}{uczen.imie} {uczen.nazwisko}{Style.RESET_ALL} z klasy {Fore.YELLOW}{uczen.klasa}{Style.RESET_ALL}: "
        )
        for nauczyciel in nauczyciele:
            if uczen.klasa in nauczyciel.klasy:
                print(
                    f"- {nauczyciel.przedmiot} (prowadzi {nauczyciel.imie} {nauczyciel.nazwisko})"
                )
    else:
        print(f"{Fore.RED}Nie znaleziono ucznia o podanych danych!{Style.RESET_ALL}")


def zarzadazaj_nauczycielem():
    imie = input("Podaj imie nauczyciela: ")
    nazwisko = input("Podaj nazwisko nauczyciela: ")
    nauczyciel = next(
        (
            nauczyciel
            for nauczyciel in nauczyciele
            if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko
        ),
        None,
    )
    if nauczyciel:
        print(
            f"Nauczyciel {Fore.CYAN}{nauczyciel.imie} {nauczyciel.nazwisko} {Style.RESET_ALL}nauczajacy {Fore.CYAN}{nauczyciel.przedmiot}{Style.RESET_ALL} prowadzi klasy: {', '.join(nauczyciel.klasy)}"
        )
    else:
        print(
            f"{Fore.RED}Nie znaleziono nauczyciela o podanych danych!{Style.RESET_ALL}"
        )


def zarzadzaj_wychowawca():
    imie = input("Podaj imie wychowawcy: ")
    nazwisko = input("Podaj nazwisko wychowawcy: ")
    wychowawca = next(
        (
            wychowawca
            for wychowawca in wychowawcy
            if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko
        ),
        None,
    )
    if wychowawca:
        uczniowe_klasa, _ = wyszukiwanie_uczniów_w_klasie(wychowawca.prowadzona_klasa)
        print(
            f"Wychowawca {Fore.CYAN}{wychowawca.imie} {wychowawca.nazwisko} {Style.RESET_ALL} prowadzi klase {Fore.CYAN}{wychowawca.prowadzona_klasa}{Style.RESET_ALL}"
        )
        print("Uczniowie tej klasy: ")
        for uczen in uczniowe_klasa:
            print(f" - {uczen}")
    else:
        print(f"{Fore.RED}Nie zaleziono wychowawcy o podanych danych!{Style.RESET_ALL}")


klasy = []
uczniowie = []
wychowawcy = []
nauczyciele = []

while True:
    wybor_uzytkownika = input(
        "Podaj działanie:\n" "1. Utwórz\n" "2. Zarządzaj\n" "3. Zakończ\n"
    )
    if wybor_uzytkownika in ("1", "Utwórz"):
        dodawanie = input(
            "Jakiego użytkownika chcesz dodać: \n"
            "1. Uczeń\n"
            "2. Nauczyciel\n"
            "3. Wychowawca\n"
        )
        if dodawanie == "1":
            imie = input("Podaj imie ucznia: ")
            nazwisko = input("Podaj nazwisko ucznia: ")
            klasa = input("Podaj klase do której chodzi uczeń: ")
            uczniowie.append(Uczen(imie, nazwisko, klasa))
        elif dodawanie == "2":
            imie = input("Podaj imie nauczyciela: ")
            nazwisko = input("Podaj nazwisko nauczyciela: ")
            przedmiot = input("Podaj przedmiot którego uczy nauczyciel: ")
            nauczyciel = Nauczyciel(imie, nazwisko, przedmiot)
            while True:
                klasa = input(
                    "Podaj nazwę klasy,którą prowadzi nauczyciel (Lub zostaw puste, aby zakonczyc): "
                )
                if klasa == "":
                    break
                nauczyciel.dodaj_klase(klasa)
            nauczyciele.append(nauczyciel)

        elif dodawanie == "3":
            imie = input("Podaj imie wychowawcy: ")
            nazwisko = input("Podaj nazwisko wychowawcy: ")
            prowadzona_klasa = input("Podaj klasę która prowadzi wychowawca: ")
            wychowawcy.append(Wychowawca(imie, nazwisko, prowadzona_klasa))

    elif wybor_uzytkownika in ("2", "Zarządzaj"):
        zarzadzanie = input(
            "Jakim typem użytkownika chcesz zarządzać: \n"
            "1. Klasa\n"
            "2. Uczeń\n"
            "3. Nauczyciel\n"
            "4. Wychowawca\n"
            "5. Koniec\n"
        )
        if zarzadzanie == "1":
            zarzadzaj_klasa()
        if zarzadzanie == "2":
            zarzadzaj_uczniem()
        if zarzadzanie == "3":
            zarzadazaj_nauczycielem()
        if zarzadzanie == "4":
            zarzadzaj_wychowawca()
        if zarzadzanie == "5":
            continue

    elif wybor_uzytkownika == "3" or wybor_uzytkownika.lower() == "zakończ":
        break
    else:
        print("Nieprawidłowa Komenda!")
