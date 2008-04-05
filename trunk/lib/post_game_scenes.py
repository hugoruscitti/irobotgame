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


class Final(Scene):

    def __init__(self, world):
        Scene.__init__(self, world)
        self.step = 0
        self._create_sprites()
        self.text = text.History("Good bye robot city...")

    def update(self, dt):
        self.step += dt

    def _create_sprites(self):
        ima_background = common.load_image('intro/sky3.png')
        layer = common.load_image('layer.png')

        sky = ActionSprite(ima_background)
        sky.y = 118
        sky.x = 100
        sky.do(Move((0, -5), 6))

        image = common.load_image('intro/castle.png')
        image.anchor_x = image.width / 2
        castle = ActionSprite(image)
        castle.x = 320
        castle.y = 100
        castle.do(Move((0, -10), 4) | Scale(0.97, 4))

        ima = common.load_image('intro/tree.png')
        ima.anchor_x = image.width / 2
        intro_1 = ActionSprite(ima)
        intro_1.x = 95 + image.width / 2
        intro_1.y = 80
        intro_1.do(Move((0, 20), 4) | Scale(1.1, 4))

        player = ActionSprite(common.load_image('intro/player.png'))
        player.x = 400
        player.y = 90

        player.do(Jump(5, 40, 5, 4))

        self.sprites = [sky, castle, intro_1, player]
        self.layer = layer

    def on_draw(self):
        self.world.clear()
        for s in self.sprites:
            s.draw()

        self.layer.blit(0, 0)

        self.text.draw()


class Regular(Scale):

    def __init__(self, world):
        Scale.__init__(self, world)

    def on_draw(self):
        pass

