import sys
from file_handler import FileHandler

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(
            "Użycie: python Manager.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    transformations = sys.argv[3:]
    handler = FileHandler(input_file, output_file, transformations)
    handler.transform()

    print("Zmienione dane:")
    handler.display_data()

    handler.save_data_to_output_file()
    print(f"Dane zapisano do pliku: {output_file}")
