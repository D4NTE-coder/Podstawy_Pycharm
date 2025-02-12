import datetime
from colorama import Fore, Style, init

from file_holder import WeatherForecast
from utils import check_rain, get_coordinates


def main():
    forecast = WeatherForecast()
    while True:
        cities_name = input("Podaj nazwę miast (oddzielone przecinkami, lub wpisz 'exit' aby zakończyć): ")
        if cities_name.lower() == "exit":
            break

        cities = [city.strip() for city in cities_name.split(",")]

        for city_name in cities:
            coordinates = get_coordinates(city_name)
            if not coordinates:
                print(f"Nie znaleziono współrzędnych dla {city_name}")
                continue

            print(f"{Fore.LIGHTBLUE_EX}Współrzędne dla miasta {city_name}: {coordinates[0]}, {coordinates[1]}{Style.RESET_ALL}")

            date_input = input("Podaj daty w formacie YYYY-MM-DD oddzielone przecinkami (domyślnie jutrzejsza data): ")
            if not date_input:
                dates = [(datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")]
            else:
                dates = [date.strip() for date in date_input.split(",")]

                for i, date in enumerate(dates):
                    try:
                        datetime.datetime.strptime(date, "%Y-%m-%d")
                    except ValueError:
                        print(f"{Fore.RED}Niepoprawny format daty: {date}. Używam domyślnej daty.{Style.RESET.ALL}")
                        dates[i] = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

            for searched_date in dates:
                if forecast.exist(city_name, searched_date):
                    result = forecast[city_name][searched_date]
                else:
                    result = check_rain(coordinates[0], coordinates[1], searched_date)
                    forecast.save(city_name, searched_date, result)

                print(f"{Fore.YELLOW}Wynik dla {city_name} ({searched_date}): {result}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
