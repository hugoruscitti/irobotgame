# -*- encoding: utf-8 -*-
from scene import Scene

class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)

    def on_draw(self):
        print "orint"
        pass
