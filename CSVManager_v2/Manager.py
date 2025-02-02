import sys
from file_handler import FileHandlerFactory


class FileProcessor:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes

        self.input_handler = FileHandlerFactory.get_handler(self.input_file)
        self.output_handler = FileHandlerFactory.get_handler(self.output_file)

    def process(self):
        data = self.input_handler.read()

        for change in self.changes:
            try:
                x, y, value = change.split(",")
                x, y = int(x), int(y)
                if 0 <= y < len(data) and 0 <= x < len(data[y]):
                    data[y][x] = value
                else:
                    print(f"Nieprawidłowa transformacja: {change} (poza zakresem)")
            except ValueError:
                print(f"Nieprawidłowy format transformacji: {change}")

        print("Zmodyfikowane dane:")
        for row in data:
            print(", ".join(map(str, row)))

        self.output_handler.write(data, self.output_file)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Użycie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    processor = FileProcessor(input_file, output_file, changes)
    processor.process()
