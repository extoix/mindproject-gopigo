from time import sleep
import perception
import movement

controlPerception = perception.Perception()
controlMovement = movement.Movement()

class BehaveForward:

    def executeBehavior(self):
        while controlPerception.lookForward() == False:
            print("I don't see anything in front of me")
            print("I will move forward")
            controlMovement.moveForward()
            sleep(3)
