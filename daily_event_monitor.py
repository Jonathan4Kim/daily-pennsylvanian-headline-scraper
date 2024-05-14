import json
import os
from datetime import datetime

class DailyEventMonitor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load()

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return {}

    def add_today(self, data_point):
        today = datetime.now().strftime("%Y-%m-%d")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if today not in self.data:
            self.data[today] = []
        self.data[today].append([timestamp, data_point])

    def save(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)
