import common
import pyglet
import config

class Audio:

    def __init__(self):
        if config.AUDIO:
            self.music = common.load_music('music/554_bebeto_Ambient_loop.mp3')
            self.music.play()

    def update(self):
        pyglet.media.dispatch_events()
