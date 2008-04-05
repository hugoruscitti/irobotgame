# -*- encoding: utf-8 -*-
import pyglet

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)


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
        self.label = pyglet.text.Label('', font_size=size, x=x, y=y,
                color=color, dpi=96)
        #pyglet.clock.schedule_interval(self._update, 0.01)


class History(AbstractText):
    "Un texto para las escenas de pantalla pequeña"

    def __init__(self, text):
        self.text = text
        self.label = pyglet.text.Label('', font_size=18, x=100, y=80, dpi=96)
        #pyglet.clock.schedule_interval(self._update, 0.01)


class BigMessage(AbstractText):
    "Un texto en el centro de la pantalla con algún mensaje rápido."

    def __init__(self, text, x=320):
        self.text = text
        self.label = pyglet.text.Label('', font_size=40, x=x, y=240, dpi=96,
                bold=True)
        #pyglet.clock.schedule_interval(self._update, 0.01)


class GameMessage(AbstractText):
    "Texto que se muestra mientras transcurre el juego."

    def __init__(self, text=''):
        self.label = pyglet.text.Label('', font_size=18, x=512, y=260, dpi=96,
                valign='center', halign='center')
        self.set_text(text)

    def set_text(self, text):
        self.label.text = text


class Score(AbstractText):
    "Un texto para las escenas de pantalla pequeña"

    def __init__(self, text):
        self.text = text
        self.label = pyglet.text.Label('', font_size=18, x=100, y=40, dpi=96)
        #pyglet.clock.schedule_interval(self._update, 0.01)


class AboutText(AbstractText):

    def __init__(self):
        self.name = pyglet.text.Label('', font_size=23, x=400, y=400, dpi=96,
                color=BLACK, bold=True)
        self.task = pyglet.text.Label('', font_size=18, x=400, y=365, dpi=96,
                color=BLACK)

    def draw(self):
        self.name.draw()
        self.task.draw()

    def set_text(self, name, task):
        self.name.text = name
        self.task.text = task

    def set_position(self, x, y):
        self.name.x = x
        self.task.x = x
        self.name.y = y
        self.task.y = y - 35
