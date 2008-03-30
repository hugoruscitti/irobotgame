# -*- encoding: utf-8 -*-
from scene import Scene
import common
import mouse
import config


class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)
        self._background = common.load_image('game_background.png')
        self.mouse = mouse.Mouse()
        self.world.set_exclusive_mouse(True)

    def on_draw(self):
        self.world.clear()            # FIXME: evitar que se tapan los bordes
        self._background.blit(0, 0)

        if config.DEBUG:
            self.mouse.draw()


    def update(self, dt):
        self.mouse.update(dt)
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        # FIXME: Creo que solo habría que actualizar el mouse cuando el tipo
        # deba mover el mouse, antes no. Por ello esto se tendría que arreglar
        # a futuro.
        self.mouse.on_mouse_motion(x, y, dx, dy)
