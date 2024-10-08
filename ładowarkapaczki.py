
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
            #dodanie przedzialu od 1 do 10 kg dopusczonej paczki
            if waga_elementu < 0.1 or waga_elementu > 10:
                print("Waga elementu nie znajduje sie w przedziale 0.1 do 10 kg.")
                break
            # sprawdzenie czy przeslyka zmieni sie w paczce
            if aktualna_waga_paczki + waga_elementu <= 20:
                aktualna_waga_paczki =+ waga_elementu
                print(f"Element o wadze {waga_elementu} został dodany do {obecna_paczka}")

            #jezeli przedmiot nie miesci sie w obecnej paczce zapisujemy go i dodajemy do nowej paczki
            else:
                paczki.append(aktualna_waga_paczki)
                print(f"Obecna paczka osiagnela {obecna_paczka} limit i została wysłana z wagą {aktualna_waga_paczki}kg")
                obecna_paczka =+ 1
                aktualna_waga_paczki = waga_elementu
                print(f"Tworzenie nowej paczki {obecna_paczka}")
            break
        except ValueError:
            print("Waga elementu elementu musi być liczbą!")