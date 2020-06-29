from playsound import playsound
import os

h = __import__('Helper')


def Play(file):
    if file != "-1" and file != -1:

        if os.path.isfile(file):
            playsound(file)
        else:
            h.log('Sound path is incorrect', 'red')
