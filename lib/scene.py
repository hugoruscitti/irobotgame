class Scene:
    "Representa una escena abstacta. Cada etapa del juego extiende esta clase."

    def __init__(self, world):
        self.world = world

    def update(self, dt):
        pass
