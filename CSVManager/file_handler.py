import csv


class FileHandler:
    def __init__(self, input_file, output_file, transformations):
        self.input_file = input_file
        self.output_file = output_file
        self.transformations = transformations
        self.data = self.load_data_from_input_file()

    def load_data_from_input_file(self):
        with open(self.input_file, mode="r") as file:
            reader = csv.reader(file)
            return [row for row in reader]

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    def transform(self):
        for transformation in self.transformations:
            try:
                x, y, value = transformation.split(",")
                x, y = int(x), int(y)
                if 0 <= y < len(self.data) and 0 <= x < len(self.data[y]):
                    self.data[y][x] = value
                else:
                    print(
                        f"Nieprawidłowa transformacja: {transformation} (poza zakresem)"
                    )
            except ValueError:
                print(f"Nieprawidłowy format transformacji: {transformation}")

    def display_data(self):
        for row in self.data:
            print(", ".join(row))
