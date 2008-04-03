# -*- coding: utf-8 -*-
import robot

class Group:

    def __init__(self):
        self.robots = [
                robot.Robot(170, 250, 0.7, 9),
                robot.Robot(40, 250, 0.7, 7),
                robot.Robot(220, 130, 1, 3),
                robot.Robot(-30, 130, 1, 1),
                ]


    def update(self, dt):
        for robot in self.robots:
            robot.update(dt)

    def draw(self):
        for robot in self.robots:
            robot.draw()

    def do_move(self, move_id, delay):
        for r in self.get_robot_dancing():
            # NOTE: Ojo, siempre el último parámetro para el robot es False,
            #       porque nunca equivoca su movimiento.
            r.change_state(robot.Motion(r, int(move_id), False, int(delay)))

    def get_robot_dancing(self):
        return [x for x in self.robots if x.dancing]

    def stop_dancing_one_robot(self):
        dancing_robots = self.get_robot_dancing()

        if not dancing_robots:
            print "Eh, esto no debe ocurrir. No se puede detener robots si ninguno está bailando."

        if dancing_robots:
            first_robot = dancing_robots[0]
            first_robot.set_angry()

    def do_dancing(self):
        robots = self.get_robot_dancing()

        for r in robots:
            r.change_state(robot.Dancing(r))
