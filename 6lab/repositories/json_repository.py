import json

class JSONRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, obj):
        with open(self.file_path, 'w') as f:
            json.dump(obj, f, default=lambda o: o.__dict__)

    def load(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return data
