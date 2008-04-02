from cocos.actions import *
import common

SPEED = 0.3

class Motion(ActionSprite):

    def __init__(self, motion, delay):
        self._load_images(motion)
        ActionSprite.__init__(self, self.img)
        self.x = 520
        self.y = 160
        self.opacity = 0
        self.motion = int(motion)
        self.delay = int(delay)
        self.do(FadeIn(SPEED) + Delay(self.delay))
        self.are_active = True
        self.timer = 0
        self.delete_me = False

    def _load_images(self, motion):
        image = common.load_image('moves/%s.png' %(motion))
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2

        fail = common.load_image('fails/%s.png' %(motion))
        fail.anchor_x = fail.width / 2
        fail.anchor_y = fail.height / 2

        self.img = image
        self.fail = fail

    def kill(self):
        self.are_active = False
        self.stop()
        speed = 0.3
        self.do(Scale(2, speed) | FadeOut(speed))

    def update(self, dt):
        self.timer += dt

        if self.timer > SPEED + self.delay:
            self.image = self.fail
            #self.do(FadeOut(SPEED))

            # TODO: esto es otro sucio hack...
            self.timer = -10
        elif 0 > self.timer > -9.5:
            self._delete()

    def _delete(self):
        self.delete_me = True
