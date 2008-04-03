# -*- encoding: utf-8 -*-
import pyglet
from cocos.actions import *

import common
from scene import Scene
import intro

class Presents(Scene):

    def __init__(self, world):
        Scene.__init__(self, world)
        self._load_images()
        self._change_state('starting')

    def _change_state(self, code):
        states = {
                'starting': (self.update_starting, self.draw_starting),
                'pyweek mention': (self.update_pyweek, self.draw_pyweek),
                }

        if code == 'starting':
            self._create_sprite_logo()
        elif code == 'pyweek mention':
            self._create_sprite_pyweek()

        self.update, self.draw = states[code]
        self.step = 0

    def _load_images(self):
        self.background = common.load_image('presents/background.png')

    def _create_sprite_logo(self):
        images = [
                common.load_image('presents/frame_1.png'),
                common.load_image('presents/frame_2.png'),
                ]

        animation = pyglet.image.Animation.from_image_sequence(images, 0.10)
        self.logo = ActionSprite(animation)
        self.logo.do(FadeIn(.5) + Delay(2))
        self.logo.x = 6
        self.logo.y = 110

    def _create_sprite_pyweek(self):
        print "Sprite pyweekekekeke"
        images = [
                common.load_image('presents/pyweek_1.png'),
                common.load_image('presents/pyweek_2.png'),
                ]

        animation = pyglet.image.Animation.from_image_sequence(images, 0.10)
        self.pyweek = ActionSprite(animation)
        self.pyweek.do(FadeIn(.5) + Delay(1) + FadeOut(1))
        self.pyweek.x = 6
        self.pyweek.y = 110

    def update_starting(self, dt):
        self.step += dt

        # TODO: Arreglar este hack: se supone que el límite para pasar a la
        #       siguiente escena debe ser la suma de todos los delays de la
        #       acción enviada a logo, es decir FadeIn, Delay y FadeOut...
        #       pero por algún motivo esa animación termina mucho después.
        #       Igualmente con 4 como límite parece funcionar, mmmm....

        if self.step > 4:
            self._change_state('pyweek mention')

    def on_draw(self):
        self.draw()

    def draw_starting(self):
        self.background.blit(0, 0)
        self.logo.draw()

    def update_pyweek(self, dt):
        self.step += dt

        if self.step > 4:
            self.skip_scene()

    def draw_pyweek(self):
        self.background.blit(0, 0)
        self.pyweek.draw()


    def skip_scene(self):
        self.world.change_scene(intro.Intro(self.world))

    def on_key_press(self, symbol, state):
        if common.is_continue_key(symbol):
            self.skip_scene()
