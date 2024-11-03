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

class uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} z klasy {self.klasa}"

class nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} jest nauczycielem {self.przedmiot}"

class wychowawca:
    def __init__(self, imie, nazwisko, prowadzona_klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.prowadzona_klasa = prowadzona_klasa

    def __repr__(self):
        return f"{self.imie} {self.nazwisko} jest wychowawcą klasy {self.prowadzona_klasa}"

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
            uczniowie.append(uczen(imie,nazwisko,klasa))
        elif dodawanie == "2":
            imie = input("Podaj imie nauczyciela: ")
            nazwisko = input("Podaj nazwisko nauczyciela: ")
            przedmiot = input("Podaj przedmiot którego uczy nauczyciel: ")
            nauczyciele.append(nauczyciel(imie,nazwisko,przedmiot))
        elif dodawanie == "3":
            imie = input("Podaj imie wychowawcy")
            nazwisko = input("Podaj nazwisko wychowawcy")
            prowadzona_klasa = input("Podaj klasę która prowadzi wychowawca")
            wychowawcy.append(wychowawca(imie,nazwisko,prowadzona_klasa))

    elif wybor_uzytkownika in ("2", "Zarządzaj"):
        pass
    elif wybor_uzytkownika in ("3", "Zakończ"):
        break
    else:

            print("Nieprawidłowa Komenda!")

