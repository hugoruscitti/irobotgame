# -*- coding: utf-8 -*-
import common

DELAY_TO_RETURN = 0.4

class Player:

    def __init__(self, x=60, y=170):
        self._load_images()
        self.set_state(5)
        self.x = 60
        self.y = 170
        self._restart()

    def _load_images(self):
        self._images = {
                1: common.load_image('player/1.png'),
                2: common.load_image('player/2.png'),
                3: common.load_image('player/3.png'),
                4: common.load_image('player/4.png'),
                5: common.load_image('player/5.png'),
                51: common.load_image('player/51.png'),
                52: common.load_image('player/52.png'),
                53: common.load_image('player/51.png'),
                6: common.load_image('player/6.png'),
                7: common.load_image('player/7.png'),
                8: common.load_image('player/8.png'),
                9: common.load_image('player/9.png'),
                }

    def set_state(self, index, reset_counter=True):
        self.state = index
        self.image = self._images[index]

        if reset_counter:
            self._restart()

    def _restart(self):
        self.step = 0.0

    def draw(self):
        self.image.blit(self.x, self.y)


    def update(self, dt):
        self.step += 0.01

        if self.step > DELAY_TO_RETURN:
            self.set_state(5)
        else:
            if self.state in [5, 51, 52]:
                sub_frame = int(self.step * 10)

                if sub_frame == 0:
                    self.set_state(5, False)
                elif sub_frame == 1:
                    self.set_state(51, False)
                elif sub_frame == 2:
                    self.set_state(52, False)
                elif sub_frame == 3:
                    self.set_state(53, False)
