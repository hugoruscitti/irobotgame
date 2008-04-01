import pyglet
from cocos.actions import *
import common
from pyglet.gl import *


window = pyglet.window.Window()

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

ima_background = common.load_image('intro/sky3.png')
layer = common.load_image('layer.png')


sky = ActionSprite(ima_background)
sky.y = 118
sky.x = 100
sky.do(Move((0, -5), 6))


image = common.load_image('intro/castle.png')
image.anchor_x = image.width / 2
castle = ActionSprite(image)
castle.x = 320
castle.y = 100
castle.do(Move((0, -10), 4) | Scale(0.97, 4))

ima = common.load_image('intro/tree.png')
ima.anchor_x = image.width / 2
intro_1 = ActionSprite(ima)
intro_1.x = 95 + image.width / 2
intro_1.y = 80
intro_1.do(Move((0, 20), 4) | Scale(1.1, 4))

player = ActionSprite(common.load_image('intro/player.png'))
player.x = 400
player.y = 90

player.do(Jump(5, 40, 5, 4))

sprites = [sky, castle, intro_1, player]
sprites_front = []

@window.event
def on_draw():

    for s in sprites:
        s.draw()

    layer.blit(0, 0)

    for s in sprites_front:
        s.draw()

pyglet.app.run()
