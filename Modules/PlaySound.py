from Helper import Helper
from playsound import playsound
import os


def Start(cfg):
    path = cfg['sound-path']
    if os.path.isfile(path):
        playsound(path)
    else:
        Helper.log('Sound path is incorrect', 'red')
