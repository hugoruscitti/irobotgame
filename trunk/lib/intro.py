# -*- encoding: utf-8 -*-
from cocos.actions import *
from scene import Scene

import common
import title
import text

class Intro(Scene):

    def __init__(self, world):
        Scene.__init__(self, world)
        self.change_subscene(SubScene1(self))
        self.world.audio.play_music('intro')

    def change_subscene(self, scene):
        self.sub_scene = scene
        self.step = 0

    def update(self, dt):
        self.step += dt

        if self.step > 4:
            self.sub_scene.next()
            self.step = 0

    def on_draw(self):
        self.sub_scene.on_draw()

    def on_key_press(self, symbol, state):
        if common.is_continue_key(symbol):
            self.skip_scene()

    def skip_scene(self):
        self.world.change_scene(title.Title(self.world))

    def on_mouse_press(self, x, y, button, extra=None):
        self.skip_scene()

class SubScene:

    def __init__(self, father):
        self.father = father
        self.layer = common.load_image('layer.png')

    def stop_all(self):
        for s in self.sprites:
            s.stop()

class SubScene1(SubScene):

    def __init__(self, father):
        SubScene.__init__(self, father)
        self._create_sprites()
        self.text = text.History("You destiny is to scape ...")

    def _create_sprites(self):
        sky = ActionSprite(common.load_image('intro/sky2.png'))
        sky.y = 118
        sky.do(Move((-100, 0), 6))

        intro_1 = ActionSprite(common.load_image('intro/intro_1.png'))
        intro_1.x = 95
        intro_1.y = 118
        intro_1.scale = 1.2
        intro_1.do(Scale(1.1, 6))

        run = ActionSprite(common.load_image('intro/run.png'))
        run.x = 400
        run.y = 80
        run.do(Scale(1.1, 6))

        self.sprites = [sky, intro_1, run]

    def on_draw(self):
        for s in self.sprites[:-1]:
            s.draw()

        self.layer.blit(0, 0)
        self.sprites[-1].draw()
        self.text.draw()

    def next(self):
        self.stop_all()
        self.father.change_subscene(SubScene2(self.father))


class SubScene2(SubScene):

    def __init__(self, father):
        SubScene.__init__(self, father)
        self._create_sprites()
        self.text = text.History("But for that is necessary a disguise...")

    def _create_sprites(self):
        sky = ActionSprite(common.load_image('intro/sky2.png'))
        sky.y = 118
        sky.x = 100
        sky.do(Move((-200, 0), 6))

        intro_1 = ActionSprite(common.load_image('intro/front.png'))
        intro_1.x = 120
        intro_1.y = 100
        intro_1.scale = 1.2

        run = ActionSprite(common.load_image('intro/rat.png'))
        run.x = -500
        run.y = 90
        run.scale = 1.5
        run.do(Jump(10, 300, 10, 0.4) + Delay(1.5) + Jump(10, 700, 10, 0.4))

        self.sprites = [sky, intro_1, run]

    def update(self, dt):
        pass

    def on_draw(self):
        for s in self.sprites:
            s.draw()

        self.layer.blit(0, 0)
        self.text.draw()

    def next(self):
        self.stop_all()
        self.father.change_subscene(SubScene3(self.father))


class SubScene3(SubScene):

    def __init__(self, father):
        SubScene.__init__(self, father)
        self._create_sprites()
        self.text = text.History("and dancing like a Robot !!!")

    def _create_sprites(self):
        sky = ActionSprite(common.load_image('intro/sky2.png'))
        sky.y = 118
        sky.do(Move((-200, 0), 6))

        walk = ActionSprite(common.load_image('intro/walk.png'))
        walk.y = 130
        walk.x = 120

        #TODO: reducir el tamaño de esta imágen, es grande al pedo.
        ima_background = common.load_image('intro/back_subscene_3.png')
        background = ActionSprite(ima_background)
        background.x = 0
        background.y = 0

        self.sprites = [sky, background, walk]

    def update(self, dt):
        pass

    def on_draw(self):
        for s in self.sprites:
            s.draw()

        self.layer.blit(0, 0)
        self.text.draw()

    def next(self):
        self.stop_all()
        world = self.father.world
        world.change_scene(title.Title(world))

