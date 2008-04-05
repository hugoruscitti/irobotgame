import pyglet
import random

import common
import config

class Audio:

    def __init__(self):
        if config.AUDIO:
            self._load_music()
            self._load_sounds()

    def _load_music(self):
        self.music_intro = pyglet.media.Player()
        self.music_intro.queue(common.load_music('music/intro.mp3'))
        self.music_intro.eos_action = 'loop'

        self.music_game = pyglet.media.Player()
        self.music_game.queue(common.load_music('music/wer.mp3'))
        self.music_game.eos_action = 'loop'

    def play_music(self, name):
        if config.AUDIO:
            self.stop_music()
            self._load_music()
            if name == 'game':
                self.music_game.play()
            else:
                self.music_intro.play()

    def stop_music(self):
        self.music_intro.pause()
        self.music_game.pause()

    def _load_sounds(self):
        self.sounds = {
                'fail': common.load_sound('sounds/fail.wav'),
                's1': common.load_sound('sounds/s1.wav'),
                's2': common.load_sound('sounds/s2.wav'),
                's3': common.load_sound('sounds/s3.wav'),
                's4': common.load_sound('sounds/s4.wav'),
                'stop': common.load_sound('sounds/stop.wav'),
                'ready': common.load_sound('sounds/ready.wav'),
                'go': common.load_sound('sounds/go.wav'),
                }

    def update(self):
        if config.AUDIO:
            pyglet.media.dispatch_events()

            if self.music_game.playing:
                self.music_game.dispatch_events()
            elif self.music_intro.playing:
                self.music_intro.dispatch_events()

    def play(self, name):
        if config.AUDIO:
            self.sounds[name].play()
            #self.sound.queue(self.sounds[name])
            #self.sound.play()

    def play_correct_move(self):
        #list = ['s1', 's2', 's3', 's4']
        list = ['s4']
        item = random.choice(list)
        self.sounds[item].play()