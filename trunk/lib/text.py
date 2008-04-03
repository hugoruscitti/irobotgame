# -*- encoding: utf-8 -*-
import pyglet

BLACK = (0, 0, 0, 255)


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
        pyglet.clock.schedule_interval(self._update, 0.01)


class History(AbstractText):
    "Un texto para las escenas de pantalla pequeña"

    def __init__(self, text):
        self.text = text
        self.label = pyglet.text.Label('', font_size=18, x=30, y=80, dpi=96)
        pyglet.clock.schedule_interval(self._update, 0.01)


class Message(AbstractText):
    "Un texto en el centro de la pantalla con algún mensaje rápido."

    def __init__(self, text):
        self.text = text
        self.label = pyglet.text.Label('', font_size=30, x=320, y=240, dpi=96)
