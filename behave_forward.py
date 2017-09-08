# After talking with Dr. Anderson may need to evaluate this behavior
# Simplify the behavior to just move forward or "cruse"
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
