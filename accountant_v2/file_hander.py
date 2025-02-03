import json

class FileHandler:
    def __init__(self, data_file, history_file):
        self.data_file = data_file
        self.history_file = history_file

    def load_data(self):
        with open(self.data_file, 'r') as file:
            return json.load(file)

    def load_history(self):
        with open(self.history_file, 'r') as file:
            return json.load(file)

    def save_data(self, balance, car_collection):
        with open(self.data_file, 'w') as file:
            json.dump({"saldo": balance, "autozbior": car_collection}, file)

    def save_history(self, history):
        with open(self.history_file, 'w') as file:
            json.dump(history, file)
