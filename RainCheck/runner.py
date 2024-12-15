import datetime
from RainCheck.file_handler import load_from_file, save_to_file
from utils import check_rain, get_coordinates


def main():
    city_name = input("Podaj nazwe miasta: ")
    coordinates = get_coordinates(city_name)
    if coordinates:
        print(f"Współrzędne miasta {city_name}: {coordinates[0]}, {coordinates[1]}")
    else:
        print(f"Nie udało się znaleźć współrzędnych dla miasta {city_name}.")

    date_input = input("Podaj date w formacie YYYY-MM-DD (domyślnie jutrzejsza data): ")

    if not date_input:
        searched_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime(
            "%Y-%m-%d"
        )
    else:
        try:
            searched_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").strftime(
                "%Y-%m-%d"
            )
        except ValueError:
            print("Niepoprawny format. Używam jutrzejszej daty")
            searched_date = (
                datetime.date.today() + datetime.timedelta(days=1)
            ).strftime("%Y-%m-%d")

    results = load_from_file()
    if searched_date in results:
        print(f"Wynik dla {searched_date} (z pliku): {results[searched_date]}")
    else:
        result = check_rain(coordinates[0], coordinates[1], searched_date)
        print(f"Wynik dla {searched_date}: {result}")
        result_data = {
            "city": city_name,
            "date": searched_date,
            "rain prediction": result,
        }
        save_to_file(result_data)


if __name__ == "__main__":
    main()
