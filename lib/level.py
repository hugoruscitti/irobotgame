# -*- encoding: utf-8 -*-
# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

import pyglet

import common
import motion

class Level:
    """Representa una nivel del juego.

    Conoce al grupo de robots que baila..."""

    def __init__(self, game):
        self._load_map()
        self.step = 0
        self.game = game
        self.group = game.group
        self.sprites = []
        self.dt = 0.0
        self._load_motion_images()

    def _load_motion_images(self):
        self.images = [
                None,
                common.load_image('moves/1.png'),
                common.load_image('moves/2.png'),
                common.load_image('moves/3.png'),
                common.load_image('moves/4.png'),
                None,
                common.load_image('moves/6.png'),
                common.load_image('moves/7.png'),
                common.load_image('moves/8.png'),
                common.load_image('moves/9.png'),
                ]

        for image in self.images:
            if image:
                image.anchor_x = 128
                image.anchor_y = 147

    def new_update(self, dt):
        self.dt += dt

        if self.dt > 0.5:
            self.update()
            self.dt -= 0.5

    def update(self):
        """Avanza en la linea de tiempo y genera movimientos si es
        necesario."""

        item = self._advance()

        if item:
            move_id, delay = item
            self.group.do_move(move_id, delay)
            image = self.images[int(move_id)]
            self.sprites.append(motion.Motion(image, move_id, delay, self))

    def _advance(self):
        self.step += 1

        if self.step < len(self.moves):
            items = (self.moves[self.step], self.timeline[self.step])

            if items[0] != ' ' or items[1] != ' ':
                return items
        else:
            self.game.on_end_level()

    def _load_map(self):
        stream = common.open('level.txt')
        lines = stream.readlines()
        stream.close()

        self.moves = lines[1].rstrip()
        self.timeline = lines[2].rstrip()
        self.moves_count = int(self.moves.replace(" ", ""))

        if len(self.moves) != len(self.timeline):
            #TODO: lanzar una excepción, tal vez...
            print "eh!, la lista de movimientos y linea de tiempo difieren."

    def get_motions_by_code(self, code):
        return [x for x in self.sprites if x.are_active and x.motion == code]

    def clear_old_sprites(self):
        "Limpia los sprites que tienen la marca 'delete_me'."
        removes = [x for x in self.sprites if x.delete_me]

        for r in removes:
            self.sprites.remove(r)

    def are_empty(self):
        with_live = [x for x in self.sprites if x.are_active]
        return len(with_live) == 0

    def on_motion_lost(self):
        self.game.on_motion_lost()

    def clear_when_fail(self):
        all = [x for x in self.sprites if x.are_active]

        for x in all:
            x.hide()

        #self.game.on_motion_lost()
