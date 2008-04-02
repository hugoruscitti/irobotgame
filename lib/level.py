# -*- encoding: utf-8 -*-
import common

class Level:

    def __init__(self):
        self._load_map()
        self.step = 0

    def get(self):
        """Avanza en la linea de tiempo y retorna el elemento actual.

        La tupla que retorna tiene el movimiento y la cantidad de segundos
        para realizarla.

        También puede retornar None si no hay movimiento para realizar."""

        return self._advance()

    def _advance(self):
        self.step += 1

        if self.step >= len(self.moves):
            # TODO: Terminar el nivel desde acá
            return None
        else:
            items = (self.moves[self.step], self.timeline[self.step])

            if items[0] == ' ' and items[1] == ' ':
                return None
            else:
                return items

    def _load_map(self):
        stream = common.open('level.txt')
        lines = stream.readlines()
        stream.close()

        self.moves = lines[1].strip()
        self.timeline = lines[2].strip()

        if len(self.moves) != len(self.timeline):
            #TODO: lanzar una excepción, tal vez...
            print "eh!, la lista de movimientos y linea de tiempo difieren."


if __name__ == '__main__':
    level = Level()
