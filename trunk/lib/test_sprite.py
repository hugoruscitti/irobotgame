# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

from cocos.actions import *
import pyglet
import common

window = pyglet.window.Window()

def hello(extra, number):
    print "Hello, ", extra, number

# Creando el sprite
image = common.load_image('player/5.png')
sprite = ActionSprite(image)
sprite.do(Place((100, 100)) + CallFuncS(hello, (1, 'd')))

@window.event
def on_draw():
    global sprite
    sprite.draw()

pyglet.app.run()
