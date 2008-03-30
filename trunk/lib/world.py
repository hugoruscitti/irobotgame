# -*- encoding: utf-8 -*-
import pyglet
from pyglet.gl import *

class World(pyglet.window.Window):

    def __init__(self):
        pyglet.window.Window.__init__(self, caption='I Robot ?')

    def run(self):
        pyglet.app.run()
