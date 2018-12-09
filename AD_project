#########################################################################

# Date: 2018/10/02

# file name: 3rd_assignment_main.py

# Purpose: this code has been generated for the 4 wheel drive body

# moving object to perform the project with line detector

# this code is used for the student only

#########################################################################

 

from car import Car

import time

import RPi.GPIO as GPIO

 

 

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

        rawData = self.car.color_getter.get_raw_data()

        red = rawData[0]

        green = rawData[1]

        blue = rawData[2]

        count = 0

        while True:

            print(rawData)

            l = self.car.line_detector.read_digital()

            rawData = self.car.color_getter.get_raw_data()

            red = rawData[0]

            green = rawData[1]

            blue = rawData[2]

            self.car.accelerator.go_forward(35)

            if 0 < self.car.distance_detector.get_distance() <= 20:

                count += 1

                print(123)

                #import GPIO_PWM_Buzzer_Example

                self.car.accelerator.stop()

                time.sleep(0)

                scale = [261.6, 293.6, 329.6]

                buzzer_pin = 8

                GPIO.setup(buzzer_pin, GPIO.OUT)

                

                p = GPIO.PWM(buzzer_pin, 100)

                p.start(5)     # start the PWM on 5% duty cycle

                for i in range(3):

                    

                    p.ChangeFrequency(scale[i])

                    time.sleep(0.5)

 

                    p.stop()  # stop the PWM output

 

                self.car.accelerator.go_forward(35)

                self.car.steering.turn(60)

                time.sleep(1.0)

                while True:

                    l = self.car.line_detector.read_digital()

                    if l == [0, 0, 0, 0, 0]:

                        self.car.steering.turn(90)

                    else:

                        break

                while True:

                    if l != [0, 0, 0, 0, 0]:

                        self.car.steering.turn(125)

                        time.sleep(1.1)

                        break

                while True:

                    l = self.car.line_detector.read_digital()

                    if l == [0, 0, 0, 0, 0]:

                        self.car.steering.turn(125)

                    else:

                        break

            elif (red < 100) and (green > 100) and (blue < 150):

                self.car.accelerator.go_forward(100)

                time.sleep(0.1)

            elif (red < 80) and (green < 110) and (blue > 120):

                self.car.accelerator.stop()

                self.car.steering.turn(60)

                time.sleep(0.1)

                self.car.steering.turn(120)

                time.sleep(0.1)

                self.car.steering.turn(60)

                time.sleep(0.1)

                self.car.steering.turn(120)

                time.sleep(0.1)

                self.car.steering.turn(60)

                time.sleep(0.1)

                self.car.steering.turn(120)

                time.sleep(0.1)

                self.car.steering.turn(60)

                time.sleep(0.1)

                self.car.steering.turn(120)

                time.sleep(0.1)

                self.car.steering.turn(60)

                self.car.accelerator.go_forward(35)

                time.sleep(0.7)

            elif (red > 100) and (green < 80) and (blue < 80) :

                self.car.accelerator.go_forward(0)

                time.sleep(3)

                self.car.steering.turn(90)

                self.car.accelerator.go_forward(35)

                time.sleep(0.3)

            elif (l == [0, 0, 0, 0, 0]) :

                self.car.steering.turn(125)

                self.car.accelerator.go_backward(30)

                time.sleep(0.4)

                self.car.steering.turn(65)

                self.car.accelerator.go_forward(30)

                time.sleep(0.15)

            elif (l == [1, 0, 0, 0, 0]):

                self.car.steering.turn(55)

                time.sleep(0.03)

            elif (l == [1, 1, 0, 0, 0]):

                self.car.steering.turn(60)

                time.sleep(0.03)

            elif (l == [0, 1, 1, 0, 0]): 

                self.car.steering.turn(80)

                time.sleep(0.03)

            elif (l == [0, 0, 1, 1, 0]):

                self.car.steering.turn(100)

                time.sleep(0.03)

            elif (l == [0, 0, 0, 1, 1]):

                self.car.steering.turn(120)

                time.sleep(0.03)

            elif (l == [0, 0, 0, 0, 1]):

                self.car.steering.turn(125)

                time.sleep(0.03)

            elif (l == [1, 1, 1, 0, 0]):

                self.car.steering.turn(80)

                time.sleep(0.03)

            elif (l == [0, 0, 1, 1, 1]):

                self.car.steering.turn(100)

                time.sleep(0.03)

            elif (l == [1, 1, 1, 1, 0]):

                self.car.steering.turn(85)

                time.sleep(0.03)

            elif (l == [0, 1, 1, 1, 1]):

                self.car.steering.turn(95)

                time.sleep(0.03)

            elif (l == [1, 1, 1, 1, 1]):

                l = self.car.line_detector.read_digital()

                if(l == [1, 1, 1, 1, 1]):

                    if count == 2:

                        self.drive_parking()

                        break

                else :

                    self.car.steering.turn(70)

                    time.sleep(0.1)

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
