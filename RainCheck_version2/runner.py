import datetime
from RainCheck_version2.file_handler import WeatherForecast
from utils import check_rain, get_coordinates


def main():
    forecast = WeatherForecast
    while True:

        cities_name = input("Podaj nazwe miast(oddzielone przecinkami, lub wpisze 'exit' aby zakonczyć):")
        if cities_name.lower() == "exit":
            break

        cities = [city.strip() for city in cities_name.split(",")]

        for city_name in cities:
            coordinates = get_coordinates(city_name)
            if not coordinates:
                print(f"Nie znaleziono koordynatów dla {city_name}")
            print(f"Współrzędne dla miasta {city_name}: {coordinates[0]}, {coordinates[1]}")



if __name__ == "__main__":
    main()
