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
SCALE_TO_REDUCE = 30.0


class Mouse:
    """Representa el control de mouse.

    El objeto evalua la posición del mouse en todo momento, cuando detecta
    que el mouse se ha movido en alguna dirección llama a '_check_motion' en
    donde el movimiento detectado se reporta directamente al persona 'player'.

    Para que este objeto ande hay que hacer 'window.set_exclusive_mouse(True)' con
    anterioridad."""

    def __init__(self, player, game):
        self.x = CENTER_X
        self.y = CENTER_Y
        self.are_in = False
        self.exit_angle = 0     # angulo de salida (cuando 'are_in' pasa a True)
        self._load_images()

        self.player = player
        self.game = game


    def draw(self):
        if config.SHOW_MOUSE:
            self.background.blit(CENTER_X, CENTER_Y)
            self.circle.blit(CENTER_X, CENTER_Y)
            self.cursor.blit(self.x, self.y)

    def post_draw(self):
        if config.SHOW_PAD:
            # TODO: Pasar los valores a constantes
            #       512 es el centro del cículo de pad
            #       160 es el centro del cículo de pad
            x = (self.x - CENTER_X) / 3 + 520
            y = (self.y - CENTER_Y) / 3 + 160
            self.mouse.blit(x, y)

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
        self.mouse = common.load_image('mouse/mouse.png')
        self.mouse.anchor_x = self.mouse.width / 2
        self.mouse.anchor_y = self.mouse.height / 2

    def on_mouse_motion(self, x, y, dx, dy):
        # NOTE: esto es una refactorización de "test_mouse.py"
        # NOTE: 'x' e 'y' no se usan, si se usa 'self.x', 'self.y' ...
        self.x += dx * config.VALUE_MOUSE_MOVE
        self.y += dy * config.VALUE_MOUSE_MOVE

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
                
            self._check_motion(angle)

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
            if bottom < angle < top:
                self.game.set_state(index)
            else:
                pass

    def _mouse_move_to_center(self):
        if config.RESTORE_MOUSE:
            self.x += (CENTER_X - self.x) / SCALE_TO_REDUCE 
            self.y += (CENTER_Y - self.y) / SCALE_TO_REDUCE

    def update(self, dt):
        self._mouse_move_to_center()

        # FIX: esto es un sucio HACK...
        self.on_mouse_motion(0, 0, 0, 0)
