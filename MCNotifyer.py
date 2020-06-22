
from datetime import datetime

scraper = __import__('czech-craft-eu')


def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


ps = scraper.PageScrapper()
current_time = datetime.now().time()
next_vote_time = ps.CanVote()

if next_vote_time == 1:
    print('You can vote')
elif next_vote_time:
    date = datetime(1, 1, 1)
    current = datetime.combine(date, current_time)
    next_vote = datetime.combine(date, next_vote_time)
    time_left = next_vote - current

    print('Time left: ', strfdelta(time_left, "{hours}h {minutes}min {seconds}s"))
    #print('Seconds: ', time_left.total_seconds())
else:
    print('Error')



