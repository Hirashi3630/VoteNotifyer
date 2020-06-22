import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime


class PageScrapper:
    def __init__(self):
        self.url = 'https://czech-craft.eu/server/skymc/vote/'

    def CanVote(self):
        page = requests.get(self.url)
        if page.status_code != 200:
            return -1

        soup = BeautifulSoup(page.content, "html.parser")
        alerts = soup.findAll("div", {"class": "alert-error"})

        if len(alerts) < 1:
            return 1
        else:
            text = alerts[0].text  # if you can vote - return time left

            only_time = ":".join(re.findall("[0-9]+", text))

            result = datetime.strptime(only_time, '%H:%M:%S').time()

            return result
