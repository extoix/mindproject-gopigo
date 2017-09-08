from time import sleep
import perception
import movement

controlPerception = perception.Perception()
controlMovement = movement.Movement()

class BehaveEscape:

    def executeBehavior(self):
        if controlPerception.lookForward() and controlPerception.lookLeft() and controlPerception.lookRight() == True:
            print("I'm trapped! Need to escape!")
            controlMovement.moveBackward();
            sleep(3)
            if controlPerception.lookLeft() == False:
                controlMovement.turnLeft()
                sleep(3)
            else:
                controlMovement.turnRight()
                sleep(3)
