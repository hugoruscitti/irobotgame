import pyglet
from cocos.actions import *

import common

class Robot(ActionSprite):

    def __init__(self, x, y, scale):
        self._load_images()
        ActionSprite.__init__(self, self.img)
        self.x = x
        self.y = y
        self.scale = scale

    def _load_images(self):
        self.img = common.load_image('robot/5.png')
        self.img.x = self.img.width / 2

    def update(self, dt):
        pass
