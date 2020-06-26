from datetime import datetime
import time

settings = __import__('CFG')
cfg = settings.CFG()

scraper = __import__(cfg.scraper_file)
h = __import__('Helper')
sound = __import__('SoundManager')


def Check():
    h.log('Checking...', 'white')
    ps = scraper.PageScrapper(cfg.scraper_file_par)
    current_time = datetime.now().time()
    next_vote_time = ps.CanVote()

    if next_vote_time == 1:
        sound.Play(cfg.sound_path)
        h.log('You can vote!', 'green')
        return cfg.repeat_interval
    elif next_vote_time:
        date = datetime(1, 1, 1)
        current = datetime.combine(date, current_time)
        next_vote = datetime.combine(date, next_vote_time)
        time_left = next_vote - current

        h.log('Time left: {0}'.format(h.strfdelta(time_left, "{hours}h {minutes}min {seconds}s")), 'yellow')
        return time_left.total_seconds()
    else:
        # raise Exception('Something went wrong with loading !')  # IP ban, server is down, don\'t have internet connection...
        h.log("Something went wrong with loading !", 'red')
        input("Press Enter to exit...")
        exit()


while 1 != 2:
    interval = Check()
    h.log('Sleeping for {0} seconds. Press CTRL+C to exit.'.format(int(interval)), 'white')
    time.sleep(interval)
