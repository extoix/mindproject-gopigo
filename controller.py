# Main controller that runs all the other behaviors
from time import sleep
import behave_forward
import behave_escape
import behave_avoid_left
import behave_avoid_right

behaveForward = behave_forward.BehaveForward()
behaveEscape = behave_escape.BehaveEscape()
behaveAvoidLeft = behave_avoid_left.BehaveAvoidLeft()
behaveAvoidRight = behave_avoid_right.BehaveAvoidRight()

while True:
    behaveForward.executeBehavior()
    behaveEscape.executeBehavior()
    behaveAvoidLeft.executeBehavior()
    behaveAvoidRight.executeBehavior()
