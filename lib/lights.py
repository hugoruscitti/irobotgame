import math
from cocos.actions import *
import common

class LightCircle(ActionSprite):

    def __init__(self):
        image = common.load_image('light_1.png')
        image.anchor_x = image.width / 2
        ActionSprite.__init__(self, image)
        self.center_x = 220
        self.center_y = 120
        self.step = 0

    def update(self, dt):
        self.step += dt * 1.5
        self.x = math.sin(self.step) * 70 + self.center_x
        self.y = math.cos(self.step) * 25 + self.center_y

class Light(ActionSprite):

    def __init__(self):
        image = common.load_image('light_2.png')
        image.anchor_x = image.width / 2
        image.anchor_y = image.height
        ActionSprite.__init__(self, image)
        self.x = 220
        self.y = 500
        self.step = 0

    def update(self, dt):
        self.step += dt * 1.5
        self.rotation = - math.degrees(math.sin(self.step)) / 3
