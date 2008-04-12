# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

from cocos.actions import *
import pyglet
import common

SPEED = 0.3

class Motion(ActionSprite):

    def __init__(self, image, motion, delay, level):
        ActionSprite.__init__(self, image)
        self.x = 640 - 128
        self.y = 147
        self.opacity = 0
        self.motion = int(motion)
        self.delay = int(delay) / 2.0
        self.do(FadeIn(SPEED) + Delay(self.delay))
        self.are_active = True
        self.timer = 0
        self.delete_me = False
        self.level = level

    def kill(self):
        self.are_active = False
        try:
            self.stop()
        except:
            pass

        speed = 0.3
        self.do(Scale(2, speed) | FadeOut(speed))
        pyglet.clock.schedule_once(self._delete, speed)

    def update(self, dt):
        self.timer += dt

        if self.are_active and self.timer > SPEED + self.delay:
            self.hide()
            self.are_active = False

            # TODO: esto es otro sucio hack...
            self.timer = -10
            self.level.on_motion_lost()

        elif 0 > self.timer > -9:
            self._delete()

    def _delete(self, dt=None):
        self.delete_me = True

    def hide(self):
        self.do(Scale(0.1, SPEED) | FadeOut(SPEED))
        self.are_active = False
