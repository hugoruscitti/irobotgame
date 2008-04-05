# -*- encoding: utf-8 -*-
# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

import config
import common
import math

CENTER_X = 420
CENTER_Y = 200
SCALE_TO_REDUCE = 6.0
FORCE = 3


class Mouse:
    """Representa el control de mouse.

    Para que este objeto ande hay que hacer
    'window.set_exclusive_mouse(True)' con anterioridad."""

    def __init__(self, player):
        self.x = CENTER_X
        self.y = CENTER_Y
        self.are_in = False
        self.exit_angle = 0     # angulo de salida (cuando 'are_in' pasa a True)

        if config.SHOW_MOUSE:
            self._load_images()

        self.player = player


    def draw(self):
        self.background.blit(CENTER_X, CENTER_Y)
        self.circle.blit(CENTER_X, CENTER_Y)
        self.cursor.blit(self.x, self.y)

    def _load_images(self):
        circle = common.load_image('mouse/circle.png')
        circle.anchor_x = circle.width / 2
        circle.anchor_y = circle.height / 2

        background = common.load_image('mouse/background.png')
        background.anchor_x = background.width / 2
        background.anchor_y = background.height / 2

        cursor = common.load_image('mouse/cursor.png')
        cursor.anchor_x = cursor.width / 2
        cursor.anchor_y = cursor.height / 2

        self.circle = circle
        self.cursor = cursor
        self.background = background

    def on_mouse_motion(self, x, y, dx, dy):
        # NOTE: esto es una refactorización de "test_mouse.py"
        # NOTE: 'x' e 'y' no se usan, si se usa 'self.x', 'self.y' ...
        self.x += dx * FORCE
        self.y += dy * FORCE

        # catetos
        op = self.y - CENTER_Y
        ad = self.x - CENTER_X
    
        angle = math.degrees(math.atan2(op, ad))

        if angle < 0:
            angle += 360

        distance_to_axis = common.get_dist((self.x, self.y), (CENTER_X, CENTER_Y))

        if distance_to_axis > 150:  # radio chico
            
            if self.are_in:
                self.are_in = False
                self.exit_angle = angle

            if distance_to_axis > 200: # radio grande
                # Restringe el mouse para que no se salga del círculo
                radian_angle = math.atan2(op, ad)
                new_op = 200 * math.sin(radian_angle)
                new_ad = 200 * math.cos(radian_angle)
                self.x = CENTER_X + new_ad
                self.y = CENTER_Y + new_op
        else:
            if not self.are_in:
                #print "Sale en: %d (e ingreso en %d)" %(angle, self.exit_angle)
                self.are_in = True

                self._check_motion(angle)

    def _check_motion(self, angle):
        """Se llama cuando concluye un movimiento.

        Este método determina el tipo de movimiento cuando se ingresa al
        cículo pequeño (y se ha llegado al grande anteriormente)."""

        pieces = [
                (6, "RIGHT", 0, 22),
                (9, "RIGHTUP", 22, 67),
                (8, "UP", 67, 112),
                (7, "LEFTUP", 112, 157),
                (4, "LEFT", 157, 202),
                (1, "LEFTDOWN", 202, 247),
                (2, "DOWN", 247, 292),
                (3, "DOWNRIGHT", 292, 337),
                (6, "RIGHT", 337, 360),
                ]

        for index, name, bottom, top in pieces:
            if bottom < angle < top and bottom < self.exit_angle < top:
                self.player.set_state(index)
                #print "Detectado evento: %s" %name
            else:
                pass

    def _mouse_move_to_center(self):
        self.x += (CENTER_X - self.x) / SCALE_TO_REDUCE 
        self.y += (CENTER_Y - self.y) / SCALE_TO_REDUCE
        pass

    def update(self, dt):
        self._mouse_move_to_center()

        # FIX: esto es un sucio HACK...
        self.on_mouse_motion(0, 0, 0, 0)
