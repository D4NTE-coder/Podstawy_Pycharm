from file_hander import FileHandler

class Manager:
    def __init__(self, data_file, history_file):
        self.file_handler = FileHandler(data_file, history_file)
        self.data = self.file_handler.load_data_from_data_file()
        self.history = self.file_handler.load_data_from_history_file()
        self.saldo = self.data.get("saldo", 0)
        self.autozbior = self.data.get("autozbior, []")
        self.commands = {}

    def assign(self, command, function):
        self.commands[command] = function

    def execute(self, command, *args):
        if command in self.commands:
            return self.commands[command](*args)
        print(f"Nieznana komenda: {command}")

    def change_balance(self, amount):
        if self.saldo + amount <0:
            print(f"Brak środków na koncie.")
            self.history.append("Próba odjęcia zbyt dużej kwoty")
