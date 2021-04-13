#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
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
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        self.car.accelerator.go_forward(15)
        while True :
            l = self.car.line_detector.read_digital()
            self.car.accelerator.go_forward(100)
            if(l == [1, 0, 0, 0, 0]):
                self.car.steering.turn(60)
                time.sleep(0.03)
            elif(l ==[1, 1, 0, 0, 0]):
                self.car.steering.turn(65)
                time.sleep(0.03)
            elif(l ==[0, 1, 1, 0, 0]):
                self.car.steering.turn(80)
                time.sleep(0.03)
            elif(l ==[0, 0, 1, 1, 0]):
                self.car.steering.turn(100)
                time.sleep(0.03)
            elif(l ==[0, 0, 0, 1, 1]):
                self.car.steering.turn(115)
                time.sleep(0.03)
            elif(l ==[0, 0, 0, 0, 1]):
                self.car.steering.turn(120)
                time.sleep(0.03)
            elif(l == [0, 0, 0, 0, 0]):
                self.drive_parking()
                break
            elif(l ==[1, 1, 1, 1, 1]):
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
