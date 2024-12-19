import json

class ConfigManager:

    @staticmethod
    def get_json_data(json_class, name):
        with open("framework/config.json", "r") as file:
            json_data = json.load(file)[json_class][name]
            return json_data