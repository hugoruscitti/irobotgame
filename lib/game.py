# -*- encoding: utf-8 -*-
from scene import Scene
import common
import mouse
import config
import player
import audio


class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)
        self._background = common.load_image('game_background.png')
        self.player = player.Player()
        self.mouse = mouse.Mouse(self.player)
        self.world.set_exclusive_mouse(True)
        self.audio = audio.Audio()

    def on_draw(self):
        self.world.clear()            # FIXME: evitar que se tapan los bordes
        self._background.blit(0, 0)
        self.player.draw()

        if config.SHOW_MOUSE:
            self.mouse.draw()

    def update(self, dt):
        self.mouse.update(dt)
        self.player.update(dt)
        self.audio.update()

    def on_mouse_motion(self, x, y, dx, dy):
        # FIXME: Creo que solo habría que actualizar el mouse cuando el tipo
        # deba mover el mouse, antes no. Por ello esto se tendría que arreglar
        # a futuro.
        self.mouse.on_mouse_motion(x, y, dx, dy)
