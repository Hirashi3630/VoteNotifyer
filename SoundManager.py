from playsound import playsound


def Play(file):
    if file != "-1" and file != -1:
        playsound(file)
