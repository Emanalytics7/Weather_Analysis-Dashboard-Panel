import pandas as pd

class DataManager:
    def __init__(self, file_path):
        self.weather = pd.read_csv(file_path)

    def get_location_data(self, location):
        return self.weather[self.weather['location_name'] == location]
    
