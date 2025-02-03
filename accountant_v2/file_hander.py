import json

class FileHandler:
    def __init__(self, data_file, history_file):
        self.data_file = data_file
        self.history_file = history_file

    def load_data_from_data_file(self):
        with open(self.data_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_data_from_history_file(self):
        with open(self.history_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_data_to_data_file(self, balance, car_collection):
        with open(self.data_file, mode="w", encoding="utf-8") as file:
            json.dump({"saldo": balance, "autozbior": car_collection}, file, ensure_ascii=False, indent=4)

    def save_data_to_history_file(self, history):
        with open(self.history_file, mode="w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)
