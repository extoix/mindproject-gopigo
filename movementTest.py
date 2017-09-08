from time import sleep
import movement

controlMovement = movement.Movement()
controlMovement.turnLeft()
sleep(1)
controlMovement.turnRight()
sleep(1)
controlMovement.moveForward()
sleep(1)
controlMovement.moveBackward()
sleep(1)
