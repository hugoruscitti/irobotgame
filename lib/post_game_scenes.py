# -*- encoding: utf-8 -*-
import pyglet 
from cocos.actions import *

from scene import Scene
import title
import game

import common
import title
import text

MSG_START = 'Press space, enter or "click" to return to title screen.'

class GameOver(Scene):

    def __init__(self, world):
        Scene.__init__(self, world)
        self.step = 0
        self._load_images()
        self.are_showing_message = False
        self.texts = []
        pyglet.clock.schedule_once(self._create_game_over_text, 3)

    def _load_images(self):
        self.ima_background = common.load_image('intro/sky.png')
        ima_mounstro = common.load_image('intro/monster.png')
        ima_mounstro.anchor_x = ima_mounstro.width / 2
        ima_mounstro.anchor_y = ima_mounstro.height / 2

        ima_personajes = common.load_image('intro/players.png')
        ima_personajes.anchor_x = ima_personajes.width / 2
        ima_personajes.anchor_y = ima_personajes.height / 2

        mounstro = ActionSprite(ima_mounstro)
        personajes = ActionSprite(ima_personajes)
        mounstro.x = 320
        mounstro.y = 240 + 30
        mounstro.scale = 0.8
        personajes.x = 320
        personajes.y = 240 + 150 / 2

        speed = 1
        mounstro.do(Scale(0.9, speed + 1) | Move((0, 20), speed + 1))
        personajes.do(Move((0, -20), speed + 1))

        self.sprites = [mounstro, personajes]

    def _create_game_over_text(self, dt):
        message_1 = text.BigMessage("Game Over", x=155)
        message_2 = text.Text(MSG_START, 160, 10, color=text.WHITE)
        self.texts.append(message_1)
        self.texts.append(message_2)

    def update(self, dt):
        pass
        
    def on_draw(self):
        self.ima_background.blit(0, 0)

        for s in self.sprites:
            s.draw()

        for text in self.texts:
            text.draw()

    def on_key_press(self, symbol, extra):
        if common.is_continue_key(symbol) or common.is_cancel_key(symbol):
            pyglet.clock.unschedule(self._create_game_over_text)
            self.world.change_scene(title.Title(self.world))
