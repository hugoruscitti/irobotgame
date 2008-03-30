# -*- encoding: utf-8 -*-
import pyglet
from pyglet.gl import *

import config
import game

class World(pyglet.window.Window):

    def __init__(self):
        pyglet.window.Window.__init__(self, caption='I Robot ?', resizable=True) 
        self._scene = None
        self.change_scene(game.Game(self))

        if config.DEBUG:
            self.set_location(400, 400)

    def run(self):
        pyglet.app.run()

    def change_scene(self, scene):
        if self._scene:
            self.pop_handlers()

        self._scene = scene
        self.push_handlers(scene)
