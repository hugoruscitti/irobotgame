# -*- encoding: utf-8 -*-
import config
import common
import math

CENTER = 200
SCALE_TO_REDUCE = 10.0


class Mouse:
    """Representa el control de mouse.

    Para que este objeto ande hay que hacer
    'window.set_exclusive_mouse(True)' con anterioridad."""

    def __init__(self):
        self.x = 200
        self.y = 200
        self.are_in = False
        self.exit_angle = 0     # angulo de salida (cuando 'are_in' pasa a True)

        if config.DEBUG:
            self._load_images()         # FIXME: Solo se llama acá, en produccion.


    def draw(self):
        self.background.blit(CENTER, CENTER)
        self.circle.blit(CENTER, CENTER)
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
        self.x += dx
        self.y += dy

        # catetos
        op = self.y - CENTER
        ad = self.x - CENTER
    
        angle = math.degrees(math.atan2(op, ad))

        if angle < 0:
            angle += 360

        distance_to_axis = common.get_dist((self.x, self.y), (CENTER, CENTER))

        if distance_to_axis > 150:  # radio chico
            
            if self.are_in:
                self.are_in = False
                self.exit_angle = angle

            if distance_to_axis > 200: # radio grande
                # Restringe el mouse para que no se salga del círculo
                radian_angle = math.atan2(op, ad)
                new_op = 200 * math.sin(radian_angle)
                new_ad = 200 * math.cos(radian_angle)
                self.x = 200 + new_ad
                self.y = 200 + new_op
        else:
            if not self.are_in:
                print "Sale en: %d (e ingreso en %d)" %(angle, self.exit_angle)
                self.are_in = True

                self._check_motion(angle)

    def _check_motion(self, angle):
        """Se llama cuando concluye un movimiento.

        Este método determina el tipo de movimiento cuando se ingresa al
        cículo pequeño (y se ha llegado al grande anteriormente)."""

        pieces = [
                ("RIGHT", 0, 22),
                ("RIGHTUP", 22, 67),
                ("UP", 67, 112),
                ("LEFTUP", 112, 157),
                ("LEFT", 157, 202),
                ("LEFTDOWN", 202, 247),
                ("DOWN", 247, 292),
                ("DOWNRIGHT", 292, 337),
                ("RIGHT", 337, 360),
                ]

        for name, bottom, top in pieces:
            if bottom < angle < top and bottom < self.exit_angle < top:
                print "Detectado evento: %s" %name
            else:
                pass

    def update(self, dt):
        self.x += (CENTER - self.x) / SCALE_TO_REDUCE 
        self.y += (CENTER - self.y) / SCALE_TO_REDUCE

        # FIX: esto es un sucio HACK...
        self.on_mouse_motion(0, 0, 0, 0)
