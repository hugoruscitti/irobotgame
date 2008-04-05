# -*- encoding: utf-8 -*-
# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

import pyglet
from pyglet import font
from pyglet.gl import *

# NOTE: This file is ugly, "pyglet.text.Label" DON'T WORK !!!

BLACK = (0, 0, 0, 1)
WHITE = (1, 1, 1, 1)
GRAY = (0.2, 0.2, 0.2, 1)

FONT_S = font.load(None, 10, dpi=96)
FONT_M = font.load(None, 18, dpi=96)
FONT_N = font.load(None, 23, dpi=96, bold=True)
FONT_T = font.load(None, 18, dpi=96, italic=True)
FONT_B = font.load(None, 40, dpi=96, bold=True)




class AbstractText:
    "Base de todos los textos. Simula que el texto se está tipeando..."

    def _update(self, dt):
        if self.text:
            first, self.text = self.text[0], self.text[1:]
            self.label.text += first

    def draw(self):
        self.label.draw()


class Text(AbstractText):
    "Un texto pequeño a modo de ayuda."

    def __init__(self, text, x, y, size=10, color=BLACK):
        self.text = text
        self.color = color
        self.label = font.Text(FONT_S, '', x=x, y=y, color=color)
        pyglet.clock.schedule_interval(self._update, 0.01)


class History(AbstractText):
    "Un texto para las escenas de pantalla pequeña"

    def __init__(self, text):
        self.text = text
        self.label = font.Text(FONT_M, '', x=100, y=80, color=WHITE)
        pyglet.clock.schedule_interval(self._update, 0.01)


class BigMessage(AbstractText):
    "Un texto en el centro de la pantalla con algún mensaje rápido."

    def __init__(self, text, x=320):
        self.text = text
        #self.label = pyglet.text.Label('', font_size=40, x=x, y=240, dpi=96,
        #        bold=True)
        self.label = font.Text(FONT_B, '', x=x, y=240, color=WHITE)
        pyglet.clock.schedule_interval(self._update, 0.01)


class GameMessage(AbstractText):
    "Texto que se muestra mientras transcurre el juego."

    def __init__(self, text=''):
        self.label = font.Text(FONT_M, '', x=512, y=260, halign='center', 
                valign='center', color=WHITE)
        #self.label = pyglet.text.Label('', font_size=18, x=512, y=260, dpi=96,
        #        valign='center', halign='center')
        self.set_text(text)
        pass

    def set_text(self, text):
        self.label.text = text
        pass


class Score(AbstractText):
    "Un texto para las escenas de pantalla pequeña"

    def __init__(self, text):
        self.text = text
        #self.label = pyglet.text.Label('', font_size=18, x=100, y=40, dpi=96)
        self.label = font.Text(FONT_M, '', x=100, y=40, color=WHITE)
        pyglet.clock.schedule_interval(self._update, 0.01)


class AboutText(AbstractText):

    def __init__(self):
        self.name = font.Text(FONT_N, '', x=400, y=400, color=BLACK)
        #self.name = pyglet.text.Label('', font_size=23, x=400, y=400, dpi=96,
        #        color=BLACK, bold=True)
        self.task = font.Text(FONT_T, '', x=400, y=365, color=GRAY)
        #self.task = pyglet.text.Label('', font_size=18, x=400, y=365, dpi=96,
        #        color=BLACK)

    def draw(self):
        self.name.draw()
        self.task.draw()
        pass

    def set_text(self, name, task):
        self.name.text = name
        self.task.text = task
        pass

    def set_position(self, x, y):
        self.name.x = x
        self.task.x = x
        self.name.y = y
        self.task.y = y - 35
