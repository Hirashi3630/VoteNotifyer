import json
import io
import os

class Settings:
    def __init__(self, file_path):
        self.file_path = file_path

        interval = data['interval']
        sfx_path = data['sfx-path']


    def Load(self):
        if os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK):
            # checks if file exists
            print("File exists and is readable")
        else:
            print("Either file is missing or is not readable, creating file...")
            with io.open(os.path.join(self.file_path, 'Accounts.json'), 'w') as db_file:
                db_file.write(json.dumps({}))

        with open(self.file_path) as config_file:
            data = json.load(config_file)



s = Settings('config.json')
s.Load()