import world
from about import About as Scene

world = world.World(start_scene=False)
world.audio.play_music('intro')
new_scene = Scene(world)
world.change_scene(new_scene)
world.run()
