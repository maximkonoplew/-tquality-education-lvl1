import json

class Datatestmanager:

    @staticmethod
    def get_json_data(json_class, name):
        with open("framework/datatest.json", "r") as file:
            json_data = json.load(file)[json_class][name]
            return json_data