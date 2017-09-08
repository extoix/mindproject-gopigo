from time import sleep
import perception
import movement

controlPerception = perception.Perception()
controlMovement = movement.Movement()

class BehaveAvoidRight:

    def executeBehavior(self):
        if controlPerception.lookRight() == False:
            print("Avoiding to the right")
            controlMovement.turnRight()
            sleep(3)
            controlPerception.lookForward()
            sleep(3)
        else:
            controlPerception.lookForward()
