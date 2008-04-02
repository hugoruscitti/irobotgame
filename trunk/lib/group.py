import robot

class Group:

    def __init__(self):
        self.robots = [
                robot.Robot(40, 250, 0.7),
                robot.Robot(220, 250, 0.7),
                ]

    def update(self, dt):
        for robot in self.robots:
            robot.update(dt)

    def draw(self):
        for robot in self.robots:
            robot.draw()
