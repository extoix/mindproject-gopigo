from gopigo import *
import grovepi

class Movement:
    def turnLeft(self):
        print("Turning left")
        enc_tgt(1,1,9)
        left_rot()

    def turnRight(self):
        print("Turning right")
        enc_tgt(1,1,10)
        right_rot()

    def moveForward(self):
        print("Moving forward")
        enc_tgt(1,1,12)
        forward()

    def moveBackward(self):
        print("Moving backward")
        enc_tgt(1,1,24)
        backward()
