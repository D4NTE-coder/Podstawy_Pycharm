import datetime
from multiprocessing.managers import Value

from utils import check_rain

def main():
    latitude = input("Podaj szerokość geograficzna (latitude): ")
    longitude = input("Podaj długość geograficzna (longitude): ")
    date_input = input("Podaj date w formacie YYYY-MM-DD (domyślnie jutrzejsza data): ")

    if not date_input:
        searched_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        try:
            searched_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Niepoprawny format. Używam jutrzejszej daty")
            searched_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

if __name__ == "__main__":
    main()