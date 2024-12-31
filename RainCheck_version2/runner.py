import datetime
from file_holder import WeatherForecast
from utils import check_rain, get_coordinates


def main():
    forecast = WeatherForecast()
    while True:

        cities_name = input("Podaj nazwę miast(oddzielone przecinkami, lub wpisz 'exit' aby zakończyć): ")
        if cities_name.lower() == "exit":
            break

        cities = [city.strip() for city in cities_name.split(",")]

        for city_name in cities:
            coordinates = get_coordinates(city_name)
            if not coordinates:
                print(f"Nie znaleziono współrzędnych dla {city_name}")
                continue
            print(f"Współrzędne dla miasta {city_name}: {coordinates[0]}, {coordinates[1]}")

            date_input = input("Podaj daty w formacie YYYY-MM-DD oddzielone przecinkami (domyślnie jutrzejsza data): ")
            if not date_input:
                dates = [(datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")]
            else:
                dates = [date.strip() for date in date_input.split(",")]

                for i, date in enumerate(dates):
                    try:
                        datetime.datetime.strptime(date, "%Y-%m-%d")
                    except ValueError:
                        print(f"Niepoprawny format daty: {date}. Używam domyślnej daty.")
                        dates[i] = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

            for searched_date in dates:
                if searched_date in forecast:
                    if forecast[searched_date]["city"] == city_name:
                        print(f"Wynik dla {city_name} ({searched_date})(z pliku): {forecast[searched_date]}")
                    else:
                        print(f"Znaleziono dane dla {searched_date}, ale dla innego miasta. Nadpisuję.")
                        result = check_rain(coordinates[0], coordinates[1], searched_date)
                        print(f"Wynik dla {city_name} ({searched_date}): {result}")
                        result_data = {searched_date: {"city": city_name, "rain prediction": result}}
                        forecast.save(result_data)
                else:
                    result = check_rain(coordinates[0], coordinates[1], searched_date)
                    print(f"Wynik dla {city_name} ({searched_date}): {result}")
                    result_data = {searched_date: {"city": city_name, "rain prediction": result}}
                    forecast.save(result_data)


if __name__ == "__main__":
    main()
