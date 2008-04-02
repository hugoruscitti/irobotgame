import pyglet
from cocos.actions import *
import common
import math
import random

'''
ima_background = common.load_image('intro/sky.png')
ima_mounstro = common.load_image('intro/monster.png')
ima_mounstro.anchor_x = ima_mounstro.width / 2
ima_mounstro.anchor_y = ima_mounstro.height / 2

ima_personajes = common.load_image('intro/players.png')
ima_personajes.anchor_x = ima_personajes.width / 2
ima_personajes.anchor_y = ima_personajes.height / 2

mounstro = ActionSprite(ima_mounstro)
personajes = ActionSprite(ima_personajes)

mounstro.x = 320
mounstro.y = 240 + 30
mounstro.scale = 0.8
personajes.x = 320
personajes.y = 240 + 150 / 2

speed = 1
mounstro.do(Scale(0.9, speed + 1) | Move((0, 20), speed + 1))
personajes.do(Move((0, -20), speed + 1))


sprites = [mounstro, personajes]
'''

step = 0
ima_player = common.load_image('title/player.png')
player = ActionSprite(ima_player)
player.x = 240
player.y = 27

ima_front = common.load_image('title/front.png')
front = ActionSprite(ima_front)

ima_robot = common.load_image('title/robot.png')
robot = ActionSprite(ima_robot)
robot.x = 30
robot.do(Repeat(Jump(3, 0, 5, 5)))

ima_left = common.load_image('title/left.png')
left = ActionSprite(ima_left)

ima_right = common.load_image('title/right.png')
right = ActionSprite(ima_right)

image_box_left = common.load_image('title/box_left.png')
image_box_left.anchor_x = image_box_left.width
box_left = ActionSprite(image_box_left)
box_left.do(Repeat(Scale(1.05, 0.2) + Scale(1, 0.2)))
box_left.x = 174

image_box_right = common.load_image('title/box_right.png')
box_right = ActionSprite(image_box_right)
box_right.x = 470

box_right.do(Repeat(Scale(1.05, 0.2) + Scale(1, 0.2)))

t1_image = common.load_image('title/t1.png')
t1 = ActionSprite(t1_image)
t1.x = 0 - 100
t1.y = 480 - 210
t1.do(Move((+100, 0), 0.5))

image_title = common.load_image('title/t2.png')
t2 = ActionSprite(image_title)
t2.y = 480
t2.do(Move((0, -210), 0.5))

image_title = common.load_image('title/t3.png')
t3 = ActionSprite(image_title)
t3.x = 100
t3.y = 480 - 210
t3.do(Move((-100, 0), 0.5))


image_over = common.load_image('title/title_over.png')
over = ActionSprite(image_over)
over.y = 275
over.opacity = 0.0

LEFT_X, LEFT_Y = 88, 82
RIGHT_X, RIGHT_Y = 388, 79



sprites = [robot, left, right, box_left, box_right, front, player, t1, t2, t3, over]
window = pyglet.window.Window()

@window.event
def on_draw():
    window.clear()
    for s in sprites:
        s.draw()

def update(dt):
    global step, left, right, over

    step += dt * 3
    left.x = LEFT_X + math.sin(step) * 5
    left.y = LEFT_Y + math.cos(step) * 5

    right.x = RIGHT_X + math.sin(-step -1) * 5
    right.y = RIGHT_Y + math.cos(-step -1) * 5

    if step > 5:
        if (step) % 6 < 2:
            over.opacity = random.randint(0, 200)
        else:
            over.opacity = 0.0


pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
