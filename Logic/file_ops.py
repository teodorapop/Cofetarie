import json


def write_file(prajituri, filename='prajituri.txt'):
    with open(filename, 'w') as f:
        json.dump(prajituri, f)


def load_file(filename='prajituri.txt'):
    with open(filename, 'r') as f:
        return json.load(f)
