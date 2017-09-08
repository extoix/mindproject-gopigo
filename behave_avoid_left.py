from time import sleep
import perception
import movement

controlPerception = perception.Perception()
controlMovement = movement.Movement()

class BehaveAvoidLeft:

    def executeBehavior(self):
        if controlPerception.lookLeft() == False:
            print("Avoiding to the left")
            sleep(3)
            controlMovement.turnLeft()
            sleep(3)
            controlPerception.lookForward()
            sleep(3)
        else:
            controlPerception.lookForward()
