from playsound import playsound


class SFX:
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        playsound(self.filename)


#sfx = SFX('sfx/notif01.wav')
#sfx.play()
