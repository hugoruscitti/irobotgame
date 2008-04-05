# -*- encoding: utf-8 -*-
import math
import random

import pyglet
from cocos.actions import *

from scene import Scene
import game
import common
import text
import presents
import about

LEFT_X, LEFT_Y = 88, 82
RIGHT_X, RIGHT_Y = 388, 79
MSG_START = 'Press space, enter or "click" to start the game.'

class Title(Scene):

    def __init__(self, world, start_music=True):
        Scene.__init__(self, world)
        self.step = 0
        self._create_sprites()
        self.background = common.load_image('black.png')
        self.text = text.Text(MSG_START, 170, 10)

        if start_music:
            self.world.audio.play_music('intro')

    def _create_sprites(self):
        player = ActionSprite(common.load_image('title/player.png'))
        player.x = 240
        player.y = 27

        robot = ActionSprite(common.load_image('title/robot.png'))
        robot.x = 30
        robot.do(Repeat(Jump(3, 0, 5, 5)))

        front = ActionSprite(common.load_image('title/front.png'))
        left = ActionSprite(common.load_image('title/left.png'))
        right = ActionSprite(common.load_image('title/right.png'))

        image_box_left = common.load_image('title/box_left.png')
        image_box_left.anchor_x = image_box_left.width
        box_left = ActionSprite(image_box_left)
        box_left.x = 174
        box_left.do(Repeat(Scale(1.05, 0.2) + Scale(1, 0.2)))

        image_box_right = common.load_image('title/box_right.png')
        box_right = ActionSprite(image_box_right)
        box_right.x = 470
        box_right.do(Repeat(Scale(1.05, 0.2) + Scale(1, 0.2)))

        t1_image = common.load_image('title/t1.png')
        t1 = ActionSprite(t1_image)
        t1.x = 0 - 100
        t1.y = 480 - 210
        t1.do(Move((+100, 0), 0.5))

        image_title = common.load_image('title/t2.png')
        t2 = ActionSprite(image_title)
        t2.y = 480
        t2.do(Move((0, -210), 0.5))

        image_title = common.load_image('title/t3.png')
        t3 = ActionSprite(image_title)
        t3.x = 100
        t3.y = 480 - 210
        t3.do(Move((-100, 0), 0.5))

        image_over = common.load_image('title/title_over.png')
        over = ActionSprite(image_over)
        over.y = 275
        over.opacity = 0.0

        self.over = over
        self.right = right
        self.left = left
        self.sprites = [robot, left, right, box_left, box_right, 
                front, player, t1, t2, t3, over]

    def update(self, dt):
        step = self.step
        left = self.left
        right = self.right
        over = self.over

        self.step += dt * 3
        left.x = LEFT_X + math.sin(step) * 5
        left.y = LEFT_Y + math.cos(step) * 5

        right.x = RIGHT_X + math.sin(-step -1) * 5
        right.y = RIGHT_Y + math.cos(-step -1) * 5

        if step > 5:
            if (step) % 6 < 2:
                over.opacity = random.randint(0, 200)
            else:
                over.opacity = 0.0

    def on_draw(self):
        self.background.blit(0, 0)

        for s in self.sprites:
            s.draw()

        self.text.draw()

    def on_mouse_press(self, x, y, bottom, extra=None):
        self.world.change_scene(game.Game(self.world))

    def on_key_press(self, symbol, extra):
        if common.is_continue_key(symbol):
            self.world.change_scene(game.Game(self.world))
        elif symbol == pyglet.window.key.R:
            self.world.change_scene(presents.Presents(self.world))
        elif symbol == pyglet.window.key.ESCAPE:
            self.world.change_scene(about.About(self.world))

