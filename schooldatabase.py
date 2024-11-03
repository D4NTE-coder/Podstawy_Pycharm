# Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.
#
# Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj, koniec.
#
# Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
# Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
# Polecenie "koniec" - Kończy działanie aplikacji.
#
# Proces tworzenia użytkowników:
#
# Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy (np. "3C")
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna, labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel, aż do otrzymania pustej linii.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna, albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
# Polecenie "koniec" - Wraca do pierwszego menu.
#
# Proces zarządzania użytkownikami:
#
# Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec. Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
# Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
# Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
# Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać wszystkie klasy, które prowadzi nauczyciel.
# Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać wszystkich uczniów, których prowadzi wychowawca.
# Polecenie "koniec" - Wraca do pierwszego menu.

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
        return f"{self.imie} {self.nazwisko} jest wychowawcą klasy {self.prowadzona_klasa}"

def wyszukiwanie_uczniów_w_klasie(nazwa_klasy):
    uczniowie_klasa = [uczen for uczen in uczniowie if uczen.klasa == nazwa_klasy]

    wychowawca_klasy = next((wychowawca for wychowawca in wychowawcy if wychowawca.prowadzona_klasa == nazwa_klasy),
                            None)
    return uczniowie_klasa, wychowawca_klasy

klasy = []
uczniowie = []
wychowawcy = []
nauczyciele = []

while True:
    wybor_uzytkownika = input("Podaj działanie:\n"
                                  "1. Utwórz\n"
                                  "2. Zarządzaj\n"
                                  "3. Zakończ\n")
    if wybor_uzytkownika in ("1", "Utwórz"):
        dodawanie = input("Jakiego użytkownika chcesz dodać: \n"
                          "1. Uczeń\n"
                          "2. Nauczyciel\n"
                          "3. Wychowawca\n")
        if dodawanie == "1":
            imie = input("Podaj imie ucznia: ")
            nazwisko = input("Podaj nazwisko ucznia: ")
            klasa = input("Podaj klase do której chodzi uczeń: ")
            uczniowie.append(Uczen(imie,nazwisko,klasa))
        elif dodawanie == "2":
            imie = input("Podaj imie nauczyciela: ")
            nazwisko = input("Podaj nazwisko nauczyciela: ")
            przedmiot = input("Podaj przedmiot którego uczy nauczyciel: ")
            nauczyciel = Nauczyciel (imie, nazwisko, przedmiot)
            while True:
                klasa = input("Podaj nazwę klasy,którą prowadzi nauczyciel (Lub zostaw puste, aby zakonczyc): ")
                if klasa =="":
                    break
                nauczyciel.dodaj_klase(klasa)
            nauczyciele.append(nauczyciel)

        elif dodawanie == "3":
            imie = input("Podaj imie wychowawcy: ")
            nazwisko = input("Podaj nazwisko wychowawcy: ")
            prowadzona_klasa = input("Podaj klasę która prowadzi wychowawca: ")
            wychowawcy.append(Wychowawca(imie,nazwisko,prowadzona_klasa))

    elif wybor_uzytkownika in ("2", "Zarządzaj"):
        zarzadzanie = input("Jakim typem użytkownika chcesz zarządzać: \n"
                            "1. Klasa\n"
                            "2. Uczeń\n"
                            "3. Nauczyciel\n"
                            "4. Wychowawca\n"
                            "5. Koniec\n")
        if zarzadzanie == "1":
            nazwa_klasy = input("Podaj Klase którą chcesz sprawdzić")
            uczniowie_klasa, wychowawca_klasy = wyszukiwanie_uczniów_w_klasie(nazwa_klasy)
            print(f"\nUczniowie w klasie {nazwa_klasy}:")
            for uczen in uczniowie_klasa:
                print(f" - {Fore.YELLOW}{uczen}{Style.RESET_ALL}")
            if wychowawca_klasy:
                print(f"Wychowawcą klasy {Fore.YELLOW} {nazwa_klasy} {Style.RESET_ALL} jest : {Fore.YELLOW}{wychowawca_klasy}")
            else:
                print(f"{Fore.RED}Ta klasa nie ma obecnie wychowawcy{Style.RESET_ALL}")
        if zarzadzanie == "2":




    elif wybor_uzytkownika in ("3", "Zakończ"):
        break
    else:
        print("Nieprawidłowa Komenda!")

