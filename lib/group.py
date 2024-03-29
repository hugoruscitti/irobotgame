# -*- coding: utf-8 -*-
# I Robot? - a dancing robot game for pyweek
#
# Copyright: 2008 Hugo Ruscitti
# License: GPL 3
# Web: http://www.losersjuegos.com.ar

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
        "Retorna True si todos los robots dejan de bailar."
        dancing_robots = self.get_robot_dancing()

        if not dancing_robots:
            print "Eh, esto no debe ocurrir. No se puede detener robots si ninguno está bailando."

        if dancing_robots:
            first_robot = dancing_robots[0]
            first_robot.set_angry()

        if not self.get_robot_dancing():
            return True

    def do_dancing(self):
        robots = self.get_robot_dancing()

        for r in robots:
            r.change_state(robot.Dancing(r))

    def get_score(self):
        return len(self.get_robot_dancing())

    def restore_dancing(self):
        for robot in self.robots:
            if not robot.dancing:
                robot.unset_angry()
                return
