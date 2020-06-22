import json
import io
import os

import requests


class Settings:
    def __init__(self, file_path):
        self.file_path = file_path

        data = self.Load()
        self.interval = data['interval']
        self.sfx_path = data['sfx-path']

    def Load(self):
        if os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK):
            # checks if file exists
            print("File exists and is readable")
        else:
            print("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(self.file_path, 'config.json'), 'w') as db_file:
                db_file.write(self.GetDefaultConfig())

        with open(self.file_path) as config_file:
            data = json.load(config_file)

        return data

    @staticmethod
    def GetDefaultConfig():
        default_config_url = 'https://raw.githubusercontent.com/Hirashi3630/VoteNotifyer/master/config.json'
        return requests.get(default_config_url).content.decode("utf-8")


s = Settings('config.json')
print(s.interval)
print(s.sfx_path)

