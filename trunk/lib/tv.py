# -*- encoding: utf-8 -*-
# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

import common
from cocos.actions import *

class Wait:

    def __init__(self, tv):
        tv.set_image(0)
        pass

    def update(self, dt):
        pass


class Dancing:

    def __init__(self, tv):
        self.tv = tv
        self.frames = [0, 1, 2, 1]
        self.step = 0

    def update(self, dt):
        self.step += dt * 5
        self.tv.set_image(self.frames[int(self.step) % 4])

class Well:

    def __init__(self, tv):
        tv.set_image(4)

    def update(self, dt):
        pass

class Fail:

    def __init__(self, tv):
        tv.set_image(3)

    def update(self, dt):
        pass


class Tv(ActionSprite):

    def __init__(self):
        self._load_images()
        ActionSprite.__init__(self, self.img[0])
        self.x = 600
        self.y = 500
        self.change_state(Wait(self))
    
    def _load_images(self):
        self.img = [
                common.load_image('tv/0.png'),
                common.load_image('tv/1.png'),
                common.load_image('tv/2.png'),
                common.load_image('tv/3.png'),
                common.load_image('tv/4.png'),
                ]

        for image in self.img:
            image.anchor_x = 164
            image.anchor_y = 184

    def update(self, dt):
        self.state.update(dt)

    def set_image(self, index):
        self.image = self.img[index]

    def change_state(self, state):
        self.state = state
