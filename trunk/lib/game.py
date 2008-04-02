# -*- encoding: utf-8 -*-
import pyglet

from cocos.actions import *

from scene import Scene
import common
import mouse
import config
import player
import level

class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)

        self._background = common.load_image('game_background.png')
        self._layer = common.load_image('game_layer.png')

        self.sprites = []

        self.player = player.Player(80, 100, world.audio)
        self.mouse = mouse.Mouse(self.player, self)
        self.world.capture_mouse()
        self.level = level.Level()
        # TODO: 'audio' debería estar en World
        # TODO: quitar los objetos 'sound' de acá. Integrar al objeto audio


        pyglet.clock.schedule_interval(self.on_update_level, 0.5)

        # TODO: Crear un módulo nuevo para esta verificación
        self.actual_move = 0

    def on_update_level(self, dt):
        item = self.level.get()

        if item:
            motion, time = item
            self._create_motion(motion, time)

    def _create_motion(self, motion, time):
        #print "Crear movimiento", motion

        image = common.load_image('moves/%s.png' %(motion))
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2
        sprite = ActionSprite(image)
        sprite.done = False
        sprite.x = 520
        sprite.y = 160
        sprite.opacity = 0
        sprite.do(FadeIn(0.3))
        self.sprites.append(sprite)

        self.actual_move = motion

    def set_state(self, index):

        if self.actual_move == str(index):
            fail = False
            sprite = self.sprites[-1]

            if not sprite.done:
                sprite.done = True
                speed = 0.3
                sprite.do(Scale(2, speed) | FadeOut(speed))
        else:
            fail = True

        if isinstance(self.player.state, player.Dancing):
            self.player.change_state(player.Motion(self.player, index, fail))

    def on_draw(self):
        self.world.clear()            # FIXME: evitar que se tapan los bordes
        self._background.blit(0, 0)
        self._layer.blit(0, 0)
        self.player.draw()
        self.mouse.draw()

        for s in self.sprites:
            s.draw()

    def update(self, dt):
        self.mouse.update(dt)
        self.player.update(dt)

    def on_mouse_motion(self, x, y, dx, dy):
        # FIXME: Creo que solo habría que actualizar el mouse cuando el tipo
        # deba mover el mouse, es decir, cuando el juego le pida hacer un
        # movimiento, antes no. Por ello esto se tendría que arreglar
        # a futuro.
        self.mouse.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, button, extra):
        self.mouse.on_mouse_motion(x, y, dx, dy)
