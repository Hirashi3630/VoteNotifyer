from datetime import datetime
from termcolor import colored


def strfdelta(tdelta, fmt):  # stringify delta time
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


def log(data, color):
    pre_text = colored("[{0}]:".format(datetime.now().strftime('%H:%M:%S')), 'white')
    text = colored(data, color)
    print(pre_text, text)
