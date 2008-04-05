import pyglet
from cocos.actions import *
import common
from pyglet.gl import *


window = pyglet.window.Window()

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

ima_background = common.load_image('intro/background.png')
layer = common.load_image('layer.png')

noise = [
        common.load_image('intro/noise_1.png'),
        common.load_image('intro/noise_2.png'),
        ]
step = 0

table = ActionSprite(common.load_image('intro/table.png'))
table.x = 110
table.y = 134

frame_1 = common.load_image('intro/child_1.png')
frame_2 = common.load_image('intro/child_2.png')

run = ActionSprite(frame_1)
#run.x = 450
run.x = 800
run.y = 44
run.do(Goto((450, 44), 0.3) | Rotate(-20, 0.3) + Rotate(+20, 0.1))

sprites = [table]
sprites_front = [run]

step_1 = 0

def update(dt):
    global frame_1, frame_2, run, step_1
    frames = [frame_1, frame_2]

    print step_1
    step_1 += 1

    run.image = frames[step_1 % 2]

@window.event
def on_draw():
    global step
    window.clear()

    step += 0.5
    ima_background.blit(95, 120)
    noise[int(step % 2)].blit(95, 120)

    for s in sprites:
        s.draw()

    layer.blit(0, 0)

    for s in sprites_front:
        s.draw()


pyglet.clock.schedule_interval(update, 0.7)
pyglet.clock.schedule_interval(lambda x: x+1, 1/60.0)
pyglet.app.run()
