# -*- encoding: utf-8 -*-
import common
import motion

class Level:

    def __init__(self):
        self._load_map()
        self.step = 0
        self.sprites = []

    def update(self):
        """Avanza en la linea de tiempo y genera movimientos si es
        necesario."""

        item = self._advance()

        if item:
            self.sprites.append(motion.Motion(*item))

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

        self.moves = lines[1].strip()
        self.timeline = lines[2].strip()

        if len(self.moves) != len(self.timeline):
            #TODO: lanzar una excepción, tal vez...
            print "eh!, la lista de movimientos y linea de tiempo difieren."

    def get_motions_by_code(self, code):
        return [x for x in self.sprites if x.are_active and x.motion == code]
