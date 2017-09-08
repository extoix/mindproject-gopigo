from gopigo import *
from time import sleep
import grovepi

# It looks like every servo and mount is off a little, so adjust and set
# these values to align the servo position
servoDegreesLeft = 180
servoDegreesRight = 30
servoDegreesForward = 100

# This is the port that the untrasonic sensor is plugged into
ultrasonicGrovePiPort = 2
distance = 20

class Perception:

    def lookForward(self):
        servo(servoDegreesForward)
        sleep(3)
        isSomethingThere = grovepi.ultrasonicRead(ultrasonicGrovePiPort) < distance
        print("Is something in front of me {}".format(isSomethingThere))
        return isSomethingThere

    def lookLeft(self):
        servo(servoDegreesLeft)
        sleep(3)
        isSomethingThere = grovepi.ultrasonicRead(ultrasonicGrovePiPort) < distance
        print("Is something to the left of me {}".format(isSomethingThere))
        return isSomethingThere

    def lookRight(self):
        servo(servoDegreesRight)
        sleep(3)
        isSomethingThere = grovepi.ultrasonicRead(ultrasonicGrovePiPort) < distance
        print("Is something to the right of me {}".format(isSomethingThere))
        return isSomethingThere
