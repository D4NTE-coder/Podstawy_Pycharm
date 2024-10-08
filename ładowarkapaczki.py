
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


