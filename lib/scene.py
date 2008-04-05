class Scene:
    "Representa una escena abstacta. Cada etapa del juego extiende esta clase."

    def __init__(self, world):
        self.world = world

    def update(self, dt):
        print "Error: se debe extender el metodo Scene.update"

    def destroy(self):
        print "Error: se debe extender el metodo Scene.destroy"

    def init(self):
        print "Cuidado: no redefine Scene.init"
