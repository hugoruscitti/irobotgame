# -*- encoding: utf-8 -*-
import math

import pyglet
from pyglet.gl import *


window = pyglet.window.Window(caption='I Robot ?')
window.set_location(400, 400)
window.set_exclusive_mouse(True)

glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
glEnable(GL_BLEND)

circle = pyglet.resource.image('circle.png')
circle.anchor_x = circle.width / 2
circle.anchor_y = circle.height / 2

background = pyglet.resource.image('background.png')
background.anchor_x = background.width / 2
background.anchor_y = background.height / 2

cursor = pyglet.resource.image('cursor.png')
cursor.anchor_x = cursor.width / 2
cursor.anchor_y = cursor.height / 2

mouse_x = 200
mouse_y = 200
mouse_in = True
mouse_exit = 0

def get_dist((x0, y0), (x1, y1)):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    return math.sqrt(dx * dx + dy * dy)

@window.event
def on_mouse_motion(x, y, dx, dy):
    global mouse_x, mouse_y, mouse_in, mouse_exit
    mouse_x += dx
    mouse_y += dy

    op = mouse_y - 200
    ad = mouse_x - 200
    angulo = math.degrees(math.atan2(op, ad))

    if angulo < 0:
        angulo += 360

    if get_dist((mouse_x, mouse_y), (200, 200)) > 150:

        if mouse_in:
            #print "Sale, en:", angulo
            mouse_in = False
            mouse_exit = angulo

        if get_dist((mouse_x, mouse_y), (200, 200)) > 200:
            angulo = math.atan2(op, ad)
            new_op = 200 * math.sin(angulo)
            new_ad = 200 * math.cos(angulo)
            mouse_x = 200 + new_ad
            mouse_y = 200 + new_op
    else:
        if not mouse_in:
            print "Sale en: %d (e ingreso en %d)" %(angulo, mouse_exit)
            mouse_in = True

            pieces = [
                    ("RIGHT", 0, 22),
                    ("RIGHTUP", 22, 67),
                    ("UP", 67, 112),
                    ("LEFTUP", 112, 157),
                    ("LEFT", 157, 202),
                    ("LEFTDOWN", 202, 247),
                    ("DOWN", 247, 292),
                    ("DOWNRIGHT", 292, 337),
                    ("RIGHT", 337, 360),
                    ]

            for name, bottom, top in pieces:
                if bottom < angulo < top and bottom < mouse_exit < top:
                    print "Detectado evento: %s" %name
                else:
                    pass



@window.event
def on_draw():
    window.clear()
    background.blit(200, 200)
    circle.blit(200, 200)
    cursor.blit(mouse_x, mouse_y)
    window.flip()
    
def acercar(dt):
    global mouse_x, mouse_y
    mouse_x += (200 - mouse_x) / 10.0
    mouse_y += (200 - mouse_y) / 10.0
    on_mouse_motion(0, 0, 0, 0)

pyglet.clock.schedule_interval(acercar, 1/100.0)
pyglet.app.run()
