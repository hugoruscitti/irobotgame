# -*- encoding: utf-8 -*-
import pyglet

from scene import Scene
import common
import mouse
import config
import player
import audio
import level

class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)
        self._background = common.load_image('game_background.png')
        self._layer = common.load_image('game_layer.png')
        self.player = player.Player()
        self.mouse = mouse.Mouse(self.player)
        self.world.capture_mouse()
        self.audio = audio.Audio()
        self.level = level.Level()

        pyglet.clock.schedule_interval(self.on_update_level, 1)

    def on_update_level(self, dt):
        self.level.get()

    def on_draw(self):
        self.world.clear()            # FIXME: evitar que se tapan los bordes
        self._background.blit(0, 0)
        self._layer.blit(0, 0)
        self.player.draw()
        self.mouse.draw()


    def update(self, dt):
        self.mouse.update(dt)
        self.player.update(dt)
        self.audio.update()

    def on_mouse_motion(self, x, y, dx, dy):
        # FIXME: Creo que solo habría que actualizar el mouse cuando el tipo
        # deba mover el mouse, es decir, cuando el juego le pida hacer un
        # movimiento, antes no. Por ello esto se tendría que arreglar
        # a futuro.
        self.mouse.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, button, extra):
        self.mouse.on_mouse_motion(x, y, dx, dy)
