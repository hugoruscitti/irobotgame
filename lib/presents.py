from cocos.actions import *

import common
from scene import Scene
import intro


class Presents(Scene):

    def __init__(self, world):
        Scene.__init__(self, world)
        self._load_image()
        self.step = 0

    def _load_image(self):
        frame_1 = common.load_image('presents/frame_1.png')
        frame_2 = common.load_image('presents/frame_2.png')
        self.background = common.load_image('presents/background.png')
        self.frames = [frame_1, frame_2]

    def update(self, dt):
        self.step += dt

        if self.step > 4:
            self.skip_scene()

    def skip_scene(self):
        self.world.change_scene(intro.Intro(self.world))

    def on_draw(self):
        self.background.blit(0, 0)
        self.frames[int((self.step * 10) % 2)].blit(0, 105)

    def on_key_press(self, symbol, state):
        if common.is_continue_key(symbol):
            self.skip_scene()
