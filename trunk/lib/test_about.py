# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

import world
from about import About as Scene

world = world.World(start_scene=False)
world.audio.play_music('intro')
new_scene = Scene(world)
world.change_scene(new_scene)
world.run()
