# -*- encoding: utf-8 -*-
# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

import pyglet
from cocos.actions import *
from pyglet.gl import *

from scene import Scene
import common
import mouse
import config
import player
import level
import effects
import group
import title
import lights
import post_game_scenes
import text
import tv


class State:

    def __init__(self, game):
        self.game = game
        self.step = 0.0


class Playing(State):

    def __init__(self, game):
        State.__init__(self, game)
        self.game.world.audio.play('go')
        self.game.world.audio.play_music('game')
        self.game.create_lights()
        game.message.set_text("Go!")
        self.game.do_update_level = True
        #pyglet.clock.schedule_interval(self.game.on_update_level, 0.5)

    def update(self, dt):
        self.game.update_all_objects(dt)

class Starting(State):

    def __init__(self, game):
        State.__init__(self, game)
        game.world.audio.stop_music()
        game.world.audio.play('ready')
        game.message.set_text("Are you ready?")
        game.do_update_level = False

    def update(self, dt):
        self.step += dt

        if self.step > 2.5:
            self.game.change_state(Playing(self.game))


class Losing(State):

    def __init__(self, game):
        State.__init__(self, game)
        game.world.audio.stop_music()
        game.player.change_state(player.Losing(self.game.player))
        pyglet.clock.unschedule(game.on_update_level)

    def update(self, dt):
        self.step += dt
        self.game.player.update(dt)

        if self.step > 2.5:
            new_scene = post_game_scenes.GameOver(self.game.world, self.game)
            self.game.world.change_scene(new_scene)


class Ending(State):

    def __init__(self, game):
        State.__init__(self, game)

    def update(self, dt):
        self.step += dt

        if self.step > 2:
            score = self.game.group.get_score()

            if score == 4:
                new_scene = post_game_scenes.Final(self.game.world, self.game)
                self.game.world.change_scene(new_scene)
            elif score == 3:
                new_scene = post_game_scenes.Regular(self.game.world, self.game)
                self.game.world.change_scene(new_scene)
            else:
                new_scene = post_game_scenes.GameOver(self.game.world, self.game)
                self.game.world.change_scene(new_scene)




class Game(Scene):
    "Escena de juego donde los personajes están en el escenario."

    def __init__(self, world):
        Scene.__init__(self, world)
        self._load_images()

        self.good_moves_combo = 0
        self.sprites = []
        self.upper_lights = []
        self.lower_ligths = []
        self.tv = tv.Tv()
        #self._create_light()

        self.player = player.Player(100, 80, self, self.tv)
        self.mouse = mouse.Mouse(self.player, self)
        self.world.capture_mouse()
        self.group = group.Group()
        self.level = level.Level(self)

        # TODO: Crear un módulo nuevo para esta verificación
        self.actual_move = 0
        self.message = text.GameMessage()
        self.change_state(Starting(self))
        self.fails = 0
        self.arrows_selected = 0

    def init(self):
        pass

    def change_state(self, state):
        self._state = state

    def _load_images(self):
        self._background = common.load_image('game_background.png')
        self._layer = common.load_image('game_layer.png')
        self._layer.anchor_x = 256

    def create_lights(self):
        sprite = lights.Light()
        self.upper_lights.append(sprite)

        sprite = lights.LightCircle()
        self.lower_ligths.append(sprite)

    def on_update_level(self, dt):
        done = self.level.update()

    def on_end_level(self):
        pyglet.clock.unschedule(self.on_update_level)
        self.change_state(Ending(self))

    def on_motion_lost(self):
        all_robot_are_angry = self.group.stop_dancing_one_robot()
        self.add_fail()
        self.good_moves_combo = 0
        self.world.audio.play('stop')

        if all_robot_are_angry:
            self.change_state(Losing(self))

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
            #self.message.set_text("Wait that arrows arrives...")
            # TODO: Avisar al usuario que no mueva tanto el MOUSE
            pass
        else:
            if isinstance(self.player.state, player.Dancing):
                self.player.change_state(player.Motion(self.player, code, fail))

                # Si falla hace que se enoje uno de los robots
                if fail:
                    self.good_moves_combo = 0
                    self.world.audio.play('stop')
                    all_robot_are_angry = self.group.stop_dancing_one_robot()
                    self.add_fail()

                    if all_robot_are_angry:
                        self.change_state(Losing(self))
                else:
                    self.arrows_selected += 1
                    self.good_moves_combo += 1

                    if self.good_moves_combo > 3:
                        self.group.restore_dancing()
                        self.good_moves_combo = 0

    def on_draw(self):
        self._background.blit(0, 0)
        self._layer.blit(640, 0)

        for light in self.lower_ligths:
            light.draw()

        self.group.draw()
        self.player.draw()
        self.mouse.draw()

        for sprite in self.sprites:
            sprite.draw()

        for light in self.upper_lights:
            light.draw()

        for motion in self.level.sprites:
            motion.draw()
        
        glColor3f(1, 1, 1)
        self.mouse.post_draw()

        self.message.draw()
        self.tv.draw()

    def update(self, dt):
        self.mouse.update(dt)
        self.tv.update(dt)
        self._state.update(dt)

        if self.do_update_level:
            self.level.new_update(dt)

    def update_all_objects(self, dt):
        self.player.update(dt)
        self.group.update(dt)

        for sprite in self.upper_lights:
            sprite.update(dt)

        for sprite in self.lower_ligths:
            sprite.update(dt)

        for sprite in self.level.sprites:
            sprite.update(dt)

        self.level.clear_old_sprites()

    def on_mouse_motion(self, x, y, dx, dy):
        # FIXME: Creo que solo habría que actualizar el mouse cuando el tipo
        # deba mover el mouse, es decir, cuando el juego le pida hacer un
        # movimiento, antes no. Por ello esto se tendría que arreglar
        # a futuro.
        self.mouse.on_mouse_motion(x, y, dx, dy)

    def on_key_press(self, symbol, extra):
        if common.is_cancel_key(symbol):
            pyglet.clock.unschedule(self.on_update_level)
            self.world.change_scene(title.Title(self.world))
        elif symbol == pyglet.window.key.F5:
            pyglet.clock.unschedule(self.on_update_level)
            self.world.change_scene(Game(self.world))

    def on_mouse_drag(self, x, y, dx, dy, button, extra):
        self.mouse.on_mouse_motion(x, y, dx, dy)

    def create_drop(self, x, y):
        self.sprites.append(effects.Drop(x, y))

    def on_player_stop_motion(self):
        self.group.do_dancing()

    def add_fail(self):
        self.fails += 1
        self.message.set_text("Fails: %d" %(self.fails))

    def get_score(self):
        return self.arrows_selected + 1

    def destroy(self):
        pass
