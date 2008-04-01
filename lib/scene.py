class Scene:
    "Representa una escena abstacta. Cada etapa del juego extiende esta clase."

    def __init__(self, world):
        self.world = world

    def update(self, dt):
        print "Error: se debe extender el metodo Scene:update"
        pass

    def destroy(self):
        pass
