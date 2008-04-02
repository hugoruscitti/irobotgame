from cocos.actions import *
import common

class Drop(ActionSprite):

    def __init__(self, x, y):
        image = common.load_image('drop.png')
        ActionSprite.__init__(self, image)
        self.x = x
        self.y = y
        speed = 0.2
        hide = FadeOut(speed)
        movedown = Move((0, -20), speed)
        self.do(movedown + (movedown | hide))

    def update(self, dt):
        pass
