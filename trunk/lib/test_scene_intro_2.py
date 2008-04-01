import pyglet
from cocos.actions import *
import common
from pyglet.gl import *


window = pyglet.window.Window()

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

ima_background = common.load_image('intro/sky2.png')
layer = common.load_image('layer.png')


sky = ActionSprite(ima_background)
sky.y = 118
sky.do(Move((-100, 0), 6))

intro_1 = ActionSprite(common.load_image('intro/front.png'))
intro_1.x = 120
intro_1.y = 100
intro_1.scale = 1.2

run = ActionSprite(common.load_image('intro/rat.png'))
run.x = -500
run.y = 90
run.scale = 1.5
run.do(Jump(10, 300, 10, 0.4) + Delay(1.5) + Jump(10, 700, 10, 0.4))

sprites = [sky, intro_1, run]
sprites_front = []

@window.event
def on_draw():

    for s in sprites:
        s.draw()

    layer.blit(0, 0)

    for s in sprites_front:
        s.draw()

pyglet.app.run()
