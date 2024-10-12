from colorama import Fore, Style, init

init(autoreset=True)

## Pobieranie liczby elementow do wysyłki
while True:
    liczba_elementow = input("Podaj liczbe elementow: ")
    try:
        liczba_elementow = int(liczba_elementow)
        if liczba_elementow > 0:
            break
        else:
            print("Liczba elementów do wysyłki nie może wynosić 0")
    except ValueError:
        print("Błąd! liczba elementow musi być liczbą całkowitą!")

## Zmienne potrzebne do wykonania zadania
paczki = []
aktualna_waga_paczki = 0
obecna_paczka = 1

## pobieranie wag paczek

for element in range(liczba_elementow):
    while True:
        waga_elementu = input(f"Podaj wage elementu {element +1} (kg): ")
        try:
            waga_elementu = float(waga_elementu)
            ## dodanie przedziału od 0.1 do 10 kg dopuszczonej paczki
            if waga_elementu < 1 or waga_elementu > 10:
                print("Waga elementu nie znajduje sie w przedziale 0.1 do 10 kg.")
                break
            ## sprawdzenie czy przeslyka zmieni sie w paczce
            if aktualna_waga_paczki + waga_elementu <= 20:
                aktualna_waga_paczki += waga_elementu
                print(f"Element o wadze {Fore.YELLOW}{waga_elementu}{Style.RESET_ALL} został dodany do {Fore.YELLOW}{obecna_paczka}")

            ## jezeli przedmiot nie miesci sie w obecnej paczce zapisujemy go i dodajemy do nowej paczki
            else:
                paczki.append((obecna_paczka, aktualna_waga_paczki))
                print(f"Obecna paczka osiagnela {Fore.YELLOW}{obecna_paczka}{Style.RESET_ALL} limit i została wysłana z wagą {Fore.YELLOW}{aktualna_waga_paczki}kg")
                obecna_paczka += 1
                aktualna_waga_paczki = waga_elementu
                print(f"Tworzenie nowej paczki {Fore.YELLOW}{obecna_paczka}")
            break
        except ValueError:
            print("Waga elementu elementu musi być liczbą!")

## wyslanie ostatniej paczki
if aktualna_waga_paczki > 0:
    paczki.append((obecna_paczka, aktualna_waga_paczki))
    print(f"Paczka {Fore.YELLOW}{obecna_paczka}{Style.RESET_ALL} zostala wysłana z wagą {Fore.YELLOW}{aktualna_waga_paczki}")


## wyświetlanie danych
separator=("-"*100)
liczba_paczek = []
suma_wag_paczek = []
suma_pustych_kilo = []
paczka_z_pustymi = []
najwiecej_pustych_kilo= []

if paczki:
    liczba_paczek = len(paczki)
    suma_wag_paczek = sum(waga for _, waga in paczki)
    suma_pustych_kilo = liczba_paczek * 20 - suma_wag_paczek
    paczka_z_pustymi = max(paczki,key=lambda x: 20 - x[1] )
    najwiecej_pustych_kilo = 20 - paczka_z_pustymi[1]

print(f"\n{Fore.BLACK}{separator}\n")
print(f"""Liczba paczek wysłanych {Fore.YELLOW}{liczba_paczek}{Style.RESET_ALL}\n
Suma wysłanych kilogramów {Fore.YELLOW}{suma_wag_paczek:.4f} kg{Style.RESET_ALL}\n
Suma wysłanych pustych kilogramów {Fore.YELLOW}{suma_pustych_kilo:.4f} kg{Style.RESET_ALL}\n
Paczka zawaierająca najwiecej pustych kilogramów to paczka: {Fore.YELLOW}{paczka_z_pustymi[0]}{Style.RESET_ALL} i zawierała ona {Fore.YELLOW}{najwiecej_pustych_kilo:.2f} kg{Style.RESET_ALL} pustych kilogramów\n
{Fore.BLACK}{separator}""")
