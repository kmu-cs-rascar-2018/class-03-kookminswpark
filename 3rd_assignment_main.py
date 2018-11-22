#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        distance = self.car.distance_detector.get_distance()
        count = 0
        while True:
            l = self.car.line_detector.read_digital()
            self.car.accelerator.go_forward(35)
            if 0 < self.car.distance_detector.get_distance() <= 25:
                count += 1
                self.car.steering.turn(60)
                time.sleep(0.7)
                while True:
                    l = self.car.line_detector.read_digital()
                    if l == [0, 0, 0, 0, 0]:
                        self.car.steering.turn(90)
                    else:
                        break
                while True:
                    if l != [0, 0, 0, 0, 0]:
                        self.car.steering.turn(125)
                        time.sleep(1.3)
                        break
                while True:
                    l = self.car.line_detector.read_digital()
                    if l == [0, 0, 0, 0, 0]:
                        self.car.steering.turn(90)
                    else:
                        break
            elif (l == [0, 0, 0, 0, 0]):
                self.car.steering.turn(120)
                self.car.accelerator.go_backward(30)
                time.sleep(0.5)
            elif (l == [1, 0, 0, 0, 0]):
                self.car.steering.turn(60)
                time.sleep(0.03)
            elif (l == [1, 1, 0, 0, 0]):
                self.car.steering.turn(65)
                time.sleep(0.03)
            elif (l == [0, 1, 1, 0, 0]):
                self.car.steering.turn(80)
                time.sleep(0.03)
            elif (l == [0, 0, 1, 1, 0]):
                self.car.steering.turn(100)
                time.sleep(0.03)
            elif (l == [0, 0, 0, 1, 1]):
                self.car.steering.turn(115)
                time.sleep(0.03)
            elif (l == [0, 0, 0, 0, 1]):
                self.car.steering.turn(120)
                time.sleep(0.03)
            elif (l == [1, 1, 1, 1, 1]):
                time.sleep(0.05)
                l = self.car.line_detector.read_digital()
                if (l == [1, 1, 1, 1, 1]):
                    if count == 4:
                        self.drive_parking()
                        break
            else:
                time.sleep(0.01)
                continue


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
