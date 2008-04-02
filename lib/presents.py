from cocos.actions import *

import common
from scene import Scene
import intro


class Presents(Scene):

    def __init__(self, world):
        Scene.__init__(self, world)
        self._create_sprites()
        self.step = 0

    def _create_sprites(self):
        image = common.load_image('presents/logo.png')
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2

        logo = ActionSprite(image)
        logo.scale = 0.0
        logo.do(Scale(1, 0.5))
        logo.x, logo.y = 120, 210

        image = common.load_image('presents/title.png')

        title = ActionSprite(image)
        title.x = 640
        title.y = 120
        title.do(Move((-350, 0), 0.5))

        self.sprites = [logo, title]

    def update(self, dt):
        self.step += dt

        if self.step > 3:
            self.skip_scene()

    def skip_scene(self):
        self.world.change_scene(intro.Intro(self.world))

    def on_draw(self):
        self.world.clear()

        for s in self.sprites:
            s.draw()

    def on_key_press(self, symbol, state):
        if common.is_continue_key(symbol):
            self.skip_scene()
