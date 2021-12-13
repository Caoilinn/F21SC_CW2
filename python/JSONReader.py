import json


class JSONReader:
    """Imports JSON data from a file and stores its"""

    @staticmethod
    def process_file(json_file):
        """Opens the JSON file and stores the read data in an array of JSON objects"""
        data = []
        try:
            with open(json_file, 'r') as f:
                for line in f:
                    data.append(json.loads(line))
        except FileNotFoundError:
            print("The file could not be found")
        return data
