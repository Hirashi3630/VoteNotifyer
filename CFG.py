import json
import io
import os

import requests

h = __import__('Helper')


class CFG:
    def __init__(self):
        self.file_path = 'config.json'

        data = self.Load()
        self.repeat_interval = data['repeat-interval']
        self.scraper_file = data['scraper-file']
        self.scraper_file_par = data['scraper-file-par']
        self.sound_path = data['sound-path']

    def Load(self):
        # check if exists - if not create and download default config
        if os.path.isfile(self.file_path) and os.access(self.file_path, os.R_OK):
            h.log("Config exists and is readable!", 'green')
        else:
            h.log("Either config is missing or is not readable, creating file...", 'yellow')
            with io.open(self.file_path, 'w') as db_file:
                db_file.write(self.GetDefaultConfig())
            h.log("Edit 'config.json' and execute 'MCNotifyer.py' again.", 'white')
            input("Press Enter to exit...")
            exit()

        # read file if everything is ok
        with open(self.file_path) as config_file:
            data = json.load(config_file)

        return data

    @staticmethod
    def GetDefaultConfig():
        default_config_url = 'https://raw.githubusercontent.com/Hirashi3630/VoteNotifyer/master/config.json'
        return requests.get(default_config_url).content.decode("utf-8")
