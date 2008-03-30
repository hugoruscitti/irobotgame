# -*- encoding: utf-8 -*-
from scene import Scene
import common

class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)
        self._background = common.load_image('game_background.png')

    def on_draw(self):
        self.world.clear()            # FIXME: evitar usar este clear por los bordes
                                      # de pantalla
        self._background.blit(0, 0)

    def update(self, dt):
        pass
