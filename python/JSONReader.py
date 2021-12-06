import json


class JSONReader():
    '''Imports JSON data from a file and stores its'''

    def __init__(self, jsonfile):
        self.jsonfile = jsonfile

    def process_file(self):
        '''Opens the JSON file and stores the read data in an array of JSON objects'''
        self.data = []
        try:
            with open(self.jsonfile, 'r') as f:
                for line in f:
                    self.data.append(json.loads(line))
        except FileNotFoundError:
            print("The file could not be found")

    def print_data(self):
        '''Prints the JSON data - DEBUG USE ONLY'''
        for i in self.data:
            print(i)
