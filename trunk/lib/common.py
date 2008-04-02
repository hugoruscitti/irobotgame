import os
import math

import pyglet


THISDIR = os.path.abspath(os.path.dirname(__file__))
DATADIR = os.path.normpath(os.path.join(THISDIR, '..', 'data'))

def load_image(path):
    return pyglet.image.load(os.path.join(DATADIR, path))

def load_music(path):
    return pyglet.media.load(os.path.join(DATADIR, path))

def load_sound(path):
    return pyglet.media.load(os.path.join(DATADIR, path), streaming=False)

def open(path):
    return file(os.path.join(DATADIR, path), "rt")

def get_dist((x0, y0), (x1, y1)):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    return math.sqrt(dx * dx + dy * dy)

def are_same_class(a, b):
    return a.__class__.__name__ == b.__class__.__name__

def is_continue_key(symbol):
    return symbol == pyglet.window.key.RETURN
