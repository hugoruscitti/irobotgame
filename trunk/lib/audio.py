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
        self.musics = {
                'intro': common.load_music('music/intro.mp3'),
                'game': common.load_music('music/wer.mp3'),
                }

        self.music = pyglet.media.Player()
        self.music.eos_action = 'loop'

    def play_music(self, name):
        if config.AUDIO:
            self.music.queue(self.musics[name])
            if self.music.playing:
                self.music.next()
            else:
                self.music.play()

    def _load_sounds(self):
        self.sound = pyglet.media.Player()
        self.sounds = {
                'fail': common.load_sound('sounds/fail.wav'),
                's1': common.load_sound('sounds/s1.wav'),
                's2': common.load_sound('sounds/s2.wav'),
                's3': common.load_sound('sounds/s3.wav'),
                's4': common.load_sound('sounds/s4.wav'),
                }

    def update(self):
        if config.AUDIO:
            pyglet.media.dispatch_events()

    def play(self, name):
        if config.AUDIO:
            self.sound.queue(self.sounds[name])
            self.sound.play()

    def play_correct_move(self):
        list = ['s1', 's2', 's3', 's4']
        item = random.choice(list)
        self.sound.queue(self.sounds[item])
        self.sound.play()