import csv
import json
import pickle
from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data, file_path):
        pass

class CSVHandler(FileHandler):
    def read(self):
        with open(self.file_path, mode="r", newline="") as file:
            return [row for row in csv.reader(file)]

    def write(self, data, file_path):
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)

class JSONHandler(FileHandler):
    def read(self):
        with open(self.file_path, mode="r") as file:
            return json.load(file)

    def write(self, data, file_path):
        with open(file_path, mode="w") as file:
            json.dump(data, file, indent=4)

class TXTHandler(FileHandler):
    def read(self):
        with open(self.file_path, mode="r") as file:
            return [line.strip().split(",") for line in file]

    def write(self, data, file_path):
        with open(file_path, mode="w") as file:
            file.writelines([",".join(map(str, row)) + "\n" for row in data])

class PickleHandler(FileHandler):
    def read(self):
        with open(self.file_path, mode="rb") as file:
            return pickle.load(file)

    def write(self, data, file_path):
        with open(file_path, mode="wb") as file:
            pickle.dump(data, file)

class FileHandlerFactory:
    @staticmethod
    def get_handler(file_path):
        extension = file_path.split(".")[-1]
        if extension == "csv":
            return CSVHandler(file_path)
        elif extension == "json":
            return JSONHandler(file_path)
        elif extension == "txt":
            return TXTHandler(file_path)
        elif extension == "pickle":
            return PickleHandler(file_path)
        else:
            raise ValueError(f"Niewspierany format pliku: {extension}")