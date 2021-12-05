import json


class JSONReader():
    def __init__(self, jsonfile):
        self.jsonfile = jsonfile

    def process_file(self):
        self.data = []
        try:
            with open(self.jsonfile, 'r') as f:
                for line in f:
                    self.data.append(json.loads(line))
        except FileNotFoundError:
            print("The file could not be found")

    def print_data(self):
        for i in self.data:
            print(i)
