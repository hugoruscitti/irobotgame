# -*- encoding: utf-8 -*-
import common
import motion

class Level:
    """Representa una nivel del juego.

    Conoce al grupo de robots que baila..."""

    def __init__(self, group):
        self._load_map()
        self.step = 0
        self.group = group
        self.sprites = []

    def update(self):
        """Avanza en la linea de tiempo y genera movimientos si es
        necesario."""

        item = self._advance()

        if item:
            move_id, delay = item
            self.group.do_move(move_id, delay)
            self.sprites.append(motion.Motion(move_id, delay))

    def _advance(self):
        self.step += 1

        if self.step < len(self.moves):
            items = (self.moves[self.step], self.timeline[self.step])

            if items[0] != ' ' or items[1] != ' ':
                return items
        else:
            # TODO: hacer algo para indicar el cambio de nivel
            print "Ha finalizado el nivel..."

    def _load_map(self):
        stream = common.open('level.txt')
        lines = stream.readlines()
        stream.close()

        self.moves = lines[1].rstrip()
        self.timeline = lines[2].rstrip()

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
