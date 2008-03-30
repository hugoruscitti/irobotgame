import os
import math

import pyglet


THISDIR = os.path.abspath(os.path.dirname(__file__))
DATADIR = os.path.normpath(os.path.join(THISDIR, '..', 'data'))

def load_image(path):
    return pyglet.image.load(os.path.join(DATADIR, path))


def get_dist((x0, y0), (x1, y1)):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    return math.sqrt(dx * dx + dy * dy)
