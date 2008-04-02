# -*- coding: utf-8 -*-
import pyglet
from cocos.actions import *
from pyglet.gl import *

import common

class State:
    "Representa un estado del baile."

    def __init__(self, robot):
        self.robot = robot

class Dancing(State):
    "Baila en su sitio."

    def __init__(self, robot):
        State.__init__(self, robot)
        self.animation = [5, 51, 5, 52, 5]
        self.step = 0

    def update(self, dt):
        self.step += dt * 5
        frame = self.animation[int(self.step) % len(self.animation)]
        self.robot.set_image(frame)

class Angry(State):

    def __init__(self, robot):
        State.__init__(self, robot)
        robot.set_image(robot.pos * 10)

    def update(self, dt):
        pass


class Motion(State):
    "Realiza un movimiento de baile."

    # TODO: quitar el último parámetro que no tiene sentido con los "Robots".
    def __init__(self, robot, move_id, fail_this_move, delay):
        State.__init__(self, robot)
        self.move_id = move_id
        self.fail_this_move = fail_this_move
        self.step = 0
        self.robot.set_image(move_id)
        self.delay = delay

    def update(self, dt):
        self.step += dt

        if self.step > self.delay:
            self.robot.change_state(Dancing(self.robot))



# TODO: Hacer que el Robot y Player extiendan una misma clase (son muy similares)
class Robot(ActionSprite):

    def __init__(self, x, y, scale, pos):
        self._load_images()
        ActionSprite.__init__(self, self._imgs[5])
        self.x = x
        self.y = y
        self.scale = scale
        self.set_image(5)
        self._restart()
        self.change_state(Dancing(self))
        self.dancing = True
        # la posición indicada con un número como en el teclado numérico.
        self.pos = pos

    def _load_images(self):
        # TODO: Re-utilizar la clase Player (o hacer una superclase sobre ambas)
        self._imgs = {
                0: common.load_image('robot/0.png'),
                1: common.load_image('robot/1.png'),
                2: common.load_image('robot/2.png'),
                3: common.load_image('robot/3.png'),
                4: common.load_image('robot/4.png'),
                5: common.load_image('robot/5.png'),
                51: common.load_image('robot/51.png'),
                52: common.load_image('robot/52.png'),
                6: common.load_image('robot/6.png'),
                7: common.load_image('robot/7.png'),
                8: common.load_image('robot/8.png'),
                9: common.load_image('robot/9.png'),
                10: common.load_image('robot/10.png'),
                30: common.load_image('robot/30.png'),
                70: common.load_image('robot/70.png'),
                90: common.load_image('robot/90.png'),
                }

    def set_image(self, index):
        self.image = self._imgs[index]
        self.scale = 0.5
        # TODO: Hay un problema al queder reescalar la imágen luego de cambiar
        #       su referencia, se ignora la llamada a 'self.scale'....

    def _restart(self):
        self.step = 0.0

    def change_state(self, new_state):
        # solo deja cambiar el estado del personaje si está Bailando
        self.state = new_state

    def draw(self):
        self.image.blit(self.x, self.y)

    def update(self, dt):
        self.step += dt
        self.state.update(dt)

    def set_angry(self):
        print "ANGRY!!!!!!!!!!!"

        if not self.dancing:
            print "Ojo!, no está bailando y le indican set_angry"

        self.dancing = False
        self.change_state(Angry(self))
