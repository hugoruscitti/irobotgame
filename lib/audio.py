import common
import pyglet
import config

class Audio:

    def __init__(self):

        if config.AUDIO:
            music = common.load_music('music/554_bebeto_Ambient_loop.mp3')

            self.player = pyglet.media.Player()
            self.player.eos_action = 'loop'
            self.player.queue(music)
            self.player.play()

    def update(self):
        pyglet.media.dispatch_events()
