# -*- coding: utf-8 -*-
import random
import pyglet
import common

DELAY_TO_RETURN = 0.4

class State:
    "Representa un estado del baile."

    def __init__(self, player):
        self.player = player

class Wait(State):
    "Espera durante un instante."

    def __init__(self, player):
        State.__init__(self, player)
        self.step = 0
        player.set_image(51)

    def update(self, dt):
        self.step += dt

        if self.step > 2:
            self.player.change_state(Dancing(self.player))

class Fail(State):
    "Espera mostrando que se ha equivocado."

    def __init__(self, player):
        State.__init__(self, player)
        self.step = 0
        player.set_image(0)
        player.game.create_drop(200, 300)

    def update(self, dt):
        self.step += dt

        if self.step > 0.3:
            self.player.change_state(Dancing(self.player))

class Dancing(State):
    "Vaila en su sitio."

    def __init__(self, player):
        State.__init__(self, player)
        self.animation = [5, 51, 52, 51]
        self.step = 0

    def update(self, dt):
        self.step += dt * 5
        frame = self.animation[int(self.step) % len(self.animation)]
        self.player.set_image(frame)

class Motion(State):
    "Realiza un movimiento de baile."

    def __init__(self, player, move_id, fail_this_move):
        State.__init__(self, player)
        self.move_id = move_id
        self.fail_this_move = fail_this_move
        self.step = 0
        self.player.set_image(move_id)

        if fail_this_move:
            player.audio.play('fail')
        else:
            player.audio.play_correct_move()

    def update(self, dt):
        self.step += dt

        if self.step > 0.2:
            if self.fail_this_move:
                self.player.change_state(Fail(self.player))
            else:
                self.player.change_state(Dancing(self.player))


class Player:
    "Representa a la protagonista del juego que baila."

    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.state = None
        self.game = game
        self.audio = game.world.audio

        self._load_images()
        self.set_image(5)
        self._restart()

        self.change_state(Dancing(self))

    def change_state(self, new_state):
        # solo deja cambiar el estado del personaje si está Bailando
        self.state = new_state

    def _load_images(self):
        self._images = {
                0: common.load_image('player/0.png'),
                1: common.load_image('player/1.png'),
                2: common.load_image('player/2.png'),
                3: common.load_image('player/3.png'),
                4: common.load_image('player/4.png'),
                5: common.load_image('player/5.png'),
                51: common.load_image('player/51.png'),
                52: common.load_image('player/52.png'),
                6: common.load_image('player/6.png'),
                7: common.load_image('player/7.png'),
                8: common.load_image('player/8.png'),
                9: common.load_image('player/9.png'),
                }

    def set_image(self, index):
        self.image = self._images[index]

    def _restart(self):
        self.step = 0.0

    def draw(self):
        self.image.blit(self.x, self.y)

    def update(self, dt):
        self.step += dt
        self.state.update(dt)
