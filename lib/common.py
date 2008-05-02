# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

import os
import math

import pygame
import pyglet


THISDIR = os.path.abspath(os.path.dirname(__file__))
DATADIR = os.path.normpath(os.path.join(THISDIR, '..', 'data'))

def load_image(path):
    return pyglet.image.load(os.path.join(DATADIR, path))

def load_music(filename):
    path = os.path.join(DATADIR, 'music', filename)
    pygame.mixer.music.load(path)
    '''
    return pyglet.media.load(os.path.join(DATADIR, path), streaming=True)
    '''

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
    return symbol in [pyglet.window.key.RETURN, pyglet.window.key.SPACE]

def is_cancel_key(symbol):
    return symbol == pyglet.window.key.ESCAPE
