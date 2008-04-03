# -*- encoding: utf-8 -*-
import pyglet
from cocos.actions import *

from scene import Scene
import common
import mouse
import config
import player
import level
import effects
import group

class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)

        self._background = common.load_image('game_background.png')
        self._layer = common.load_image('game_layer.png')

        self.sprites = []

        self.player = player.Player(100, 80, self)
        self.mouse = mouse.Mouse(self.player, self)
        self.world.capture_mouse()
        self.group = group.Group()
        self.level = level.Level(self.group)

        pyglet.clock.schedule_interval(self.on_update_level, 0.5)

        # TODO: Crear un módulo nuevo para esta verificación
        self.actual_move = 0

    def on_update_level(self, dt):
        self.level.update()

    def set_state(self, code):
        motions = self.level.get_motions_by_code(code)

        if motions:
            for m in motions:
                m.kill()

            fail = False
        else:
            fail = True

        # En caso de fallar y que no existan flechas evita que pieda
        if fail and self.level.are_empty():
            # TODO: Avisar al usuario que no mueva tanto el MOUSE
            pass
        else:
            if isinstance(self.player.state, player.Dancing):
                self.player.change_state(player.Motion(self.player, code, fail))

                # Si falla hace que se enoje uno de los robots
                if fail:
                    self.group.stop_dancing_one_robot()

    def on_draw(self):
        self._background.blit(0, 0)
        self._layer.blit(0, 0)
        self.group.draw()
        self.player.draw()
        self.mouse.draw()

        for sprite in self.sprites:
            sprite.draw()

        for motion in self.level.sprites:
            motion.draw()

    def update(self, dt):
        self.mouse.update(dt)
        self.player.update(dt)
        self.group.update(dt)

        for sprite in self.level.sprites:
            sprite.update(dt)

        self.level.clear_old_sprites()

    def on_mouse_motion(self, x, y, dx, dy):
        # FIXME: Creo que solo habría que actualizar el mouse cuando el tipo
        # deba mover el mouse, es decir, cuando el juego le pida hacer un
        # movimiento, antes no. Por ello esto se tendría que arreglar
        # a futuro.
        self.mouse.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, button, extra):
        self.mouse.on_mouse_motion(x, y, dx, dy)

    def create_drop(self, x, y):
        self.sprites.append(effects.Drop(x, y))

    def on_player_stop_motion(self):
        self.group.do_dancing()

