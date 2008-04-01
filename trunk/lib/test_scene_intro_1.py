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

intro_1 = ActionSprite(common.load_image('intro/intro_1.png'))
intro_1.x = 95
intro_1.y = 118
intro_1.scale = 1.2
intro_1.do(Scale(1.1, 6))

run = ActionSprite(common.load_image('intro/run.png'))
run.x = 400
run.y = 80
run.do(Scale(1.1, 6))

sprites = [sky, intro_1]
sprites_front = [run]

@window.event
def on_draw():

    for s in sprites:
        s.draw()

    layer.blit(0, 0)

    for s in sprites_front:
        s.draw()

pyglet.app.run()
