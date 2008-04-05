# -*- encoding: utf-8 -*-
import pyglet
from cocos.actions import *

import common
from scene import Scene
import intro

import text

MSG_FULLSCREEN = "Press 'f' key to alternate fullscreen / window."

class Presents(Scene):

    def __init__(self, world):
        Scene.__init__(self, world)
        self._create_sprites()
        self.background = common.load_image('presents/background.png')
        self.step = 0.0
        self.text = text.Text(MSG_FULLSCREEN, 180, 10)

    def init(self):
        pass

    def _create_sprites(self):
        images = [
                common.load_image('presents/frame_1.png'),
                common.load_image('presents/frame_2.png'),
                ]
        
        actions = FadeIn(.5) + Delay(2) + FadeOut(1)

        animation = pyglet.image.Animation.from_image_sequence(images, 0.10)
        self.logo = ActionSprite(animation)
        self.logo.do(actions)
        self.logo.x = 0
        self.logo.y = 0

        images = [
                common.load_image('presents/pyweek_1.png'),
                common.load_image('presents/pyweek_2.png'),
                ]

        animation = pyglet.image.Animation.from_image_sequence(images, 0.10)
        self.pyweek = ActionSprite(animation)
        self.pyweek.opacity = 0
        self.pyweek.do(Delay(2.5) + actions)
        self.pyweek.x = 0
        self.pyweek.y = 0

    def on_draw(self):
        self.background.blit(0, 0)
        self.logo.draw()
        self.pyweek.draw()
        self.text.draw()

    def update(self, dt):
        # TODO: Evitar la comprobación constante. Una solución podría ser
        #       utilizar la acción "CallFuncS", pero no está funcionando con
        #       métodos... parece que solo opera con funciones.
        if not self.pyweek.scheduled:
            self.skip_scene()

    def skip_scene(self):
        self.pyweek.stop()
        self.logo.stop()
        self.world.change_scene(intro.Intro(self.world))

    def on_key_press(self, symbol, state):
        if common.is_continue_key(symbol):
            self.skip_scene()

    def on_mouse_press(self, x, y, button, extra=None):
        self.skip_scene()

