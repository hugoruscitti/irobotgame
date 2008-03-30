import pyglet
from cocos.actions import *
import common


ima_mounstro = common.load_image('intro/monster.png')
ima_mounstro.anchor_x = ima_mounstro.width / 2
ima_mounstro.anchor_y = ima_mounstro.height / 2

ima_personajes = common.load_image('intro/players.png')
ima_personajes.anchor_x = ima_personajes.width / 2
ima_personajes.anchor_y = ima_personajes.height / 2

mounstro = ActionSprite(ima_mounstro)
personajes = ActionSprite(ima_personajes)

mounstro.x = 320
mounstro.y = 240
personajes.x = 320
personajes.y = 240 + 150 / 2


speed = 1
mounstro.do(Scale(1.1, speed + 1) | Move((0, 20), speed + 1))
personajes.do(Move((0, -40), speed))



sprites = [mounstro, personajes]

window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()
    for s in sprites:
        s.draw()

pyglet.app.run()
