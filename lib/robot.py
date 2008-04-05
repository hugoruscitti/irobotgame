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
        self.animation = [51, 5, 52, 5]
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
        # la posición indicada con un número como en el teclado numérico.
        self.pos = pos
        self._load_images()
        ActionSprite.__init__(self, self._imgs[5])
        self.x = x
        self.y = y
        self.scale = scale
        self.set_image(5)
        self._restart()
        self.change_state(Dancing(self))
        self.dancing = True

    def _load(self, index):
        if self.pos in [7, 9]:
            path = 'back_robot'
        else:
            path = 'robot'

        return common.load_image('%s/%d.png' %(path, index))


    def _load_images(self):
        # TODO: Re-utilizar la clase Player (o hacer una superclase sobre ambas)
        self._imgs = {
                1: self._load(1),
                2: self._load(2),
                3: self._load(3),
                4: self._load(4),
                5: self._load(5),
                51: self._load(51),
                52: self._load(52),
                6: self._load(6),
                7: self._load(7),
                8: self._load(8),
                9: self._load(9),
                10: self._load(10),
                30: self._load(30),
                70: self._load(70),
                90: self._load(90),
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
        if not self.dancing:
            print "Ojo!, no está bailando y le indican set_angry."

        self.dancing = False
        self.change_state(Angry(self))

    def unset_angry(self):
        self.dancing = True
        self.change_state(Dancing(self))
