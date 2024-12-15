import json


def save_to_file(data, filename="results.json"):
    try:
        with open(filename, "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    existing_data.update(data)

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)


def load_from_file(filename="results.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
