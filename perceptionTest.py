from time import sleep
import perception

controlPerception = perception.Perception()
controlPerception.lookForward()
sleep(2)
controlPerception.lookLeft()
sleep(2)
controlPerception.lookRight()
sleep(2)
controlPerception.lookForward()
sleep(2)
