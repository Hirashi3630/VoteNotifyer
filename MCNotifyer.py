from Helper import Helper
from datetime import datetime
import time
from pathlib import Path
import importlib
import os

settings = __import__('CFG')
cfg = settings.CFG()

scraper = __import__(cfg.scraper_file)


def CheckForVote():
    Helper.log('Checking...', 'white')
    ps = scraper.PageScrapper(cfg.scraper_file_par)
    current_time = datetime.now().time()
    next_vote_time = ps.CanVote()
    url = ps.url

    if next_vote_time == 1:
        CheckModules()
        # print to console
        Helper.log('You can vote!', 'green')
        return cfg.repeat_interval
    elif next_vote_time:
        date = datetime(1, 1, 1)
        current = datetime.combine(date, current_time)
        next_vote = datetime.combine(date, next_vote_time)
        time_left = next_vote - current

        Helper.log('Time left: {0} (at {1})'.format(Helper.strfdelta(time_left, "{hours}h {minutes}min {seconds}s"),
                                                    next_vote_time), 'yellow')
        return time_left.total_seconds()
    else:
        Helper.log("Something went wrong with loading !", 'red')  # IP ban/server is down/don't have internet connection
        input("Press Enter to exit...")
        exit()


def CheckModules():
    for path in Path('Modules').rglob('*.py'):

        module_name = os.path.splitext(path.name)[0]  # get module's name

        if not cfg.data['modules'][module_name]['enabled']:  # check if module is disabled -> break
            break

        # Helper.log('Found {0} module!'.format(module_name), 'green')
        new_module = importlib.import_module("Modules." + module_name)
        new_module.Start(cfg.data['modules'][module_name])  # call Start() method with config as parameter
        # Helper.log('{0} finished!'.format(module_name), 'green')


while True:
    interval = CheckForVote()
    Helper.log('Sleeping for {0} seconds. Press CTRL+C to exit.'.format(int(interval)), 'white')
    time.sleep(interval)
