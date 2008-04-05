# -*- encoding: utf-8 -*-
import sys

import pyglet

import text
from scene import Scene
from cocos.actions import *
import random
import common


class About(Scene):
    
    def __init__(self, world):
        Scene.__init__(self, world)
        self.step = 0
        self._load_background()
        self.name = text.AboutText()
        self.show_name = {
                'hugoruscitti': self.show_hugoruscitti,
                'cristian': self.show_cristian,
                'walter': self.show_walter,
                'javi': self.show_javi,
                }
        self._create_sprites()

        pyglet.clock.schedule_once(self.show_losersjuegos_logo, 4 + 3 * 2)

    def show_losersjuegos_logo(self, dt):
        images = [
                common.load_image('presents/frame_1.png'),
                common.load_image('presents/frame_2.png'),
                ]

        animation = pyglet.image.Animation.from_image_sequence(images, 0.10)
        
        self.logo = ActionSprite(animation)
        self.logo.opacity = 0
        self.logo.x = 0
        self.logo.y = 0
        self.logo.do(FadeIn(2))
        self.sprites.insert(0, self.logo)
        self.name.set_text('Thanks !', 'http://www.losersjuegos.com.ar')
        self.name.set_position(180, 400)

    def show_hugoruscitti(self, dt):
        self.name.set_text('Hugo Ruscitti', 'Programming')
        self.name.set_position(320, 330)

    def show_cristian(self, dt):
        self.name.set_text('Cristian Villalba', 'Programming and musics')
        self.name.set_position(290, 230)

    def show_walter(self, dt):
        self.name.set_text('Walter Velazquez', 'Art')
        self.name.set_position(320, 350)

    def show_javi(self, dt):
        self.name.set_text('Javier Da Silva', 'Art')
        self.name.set_position(280, 340)

    def _load_background(self):
        images = [
                common.load_image('about/1.png'),
                common.load_image('about/2.png'),
                ]

        animation = pyglet.image.Animation.from_image_sequence(images, 0.10)
        self.animation = ActionSprite(animation)
        self.animation.x = 0
        self.animation.y = 0

    def hide_text(self, dt):
        self.name.set_text('', '')

    def _create_sprites(self):
        self.names = ['hugoruscitti', 'cristian', 'walter', 'javi']
        random.shuffle(self.names)
        self.sprites = []

        for index, name in enumerate(self.names):
            image = common.load_image('about/%s.png' %name)
            sprite = ActionSprite(image)
            sprite.x = 50
            sprite.y = - image.height
            sprite.opacity = 0
            SPEED = 0.5
            pyglet.clock.schedule_once(self.show_name[name], 1.5 + index * 2 + 1)
            pyglet.clock.schedule_once(self.hide_text, 2.5 + index * 2 + 1)
            sprite.do(Delay(index * 2) + Delay(1) +  
                    (FadeIn(SPEED) | Move((0, image.height), SPEED)) +
                    Delay(1) + 
                    (Scale(0.3, 1) | Move((350 - index * 70, 0), 1)))

            self.sprites.append(sprite)


    def update(self, dt):
        self.step += dt

    def on_draw(self):
        self.animation.draw()

        for sprite in self.sprites:
            sprite.draw()

        self.name.draw()

    def _exit(self):
        sys.exit(0)

    def on_mouse_press(self, x, y, bottom, extra=None):
        self._exit()

    def on_key_press(self, symbol, extra):
        if common.is_continue_key(symbol):
            self._exit()
        elif symbol == pyglet.window.key.ESCAPE:
            self._exit()
