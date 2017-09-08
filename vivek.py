#!/usr/bin/env python

from random import randint
from gopigo import *
from time import sleep
import grovepi
import scan_environment
ultrasonic_ranger = 2
enable_servo()
set_speed(50)
servo(115)
no = []
a = 0

while grovepi.ultrasonicRead(ultrasonic_ranger) < 300:
    try:
        
        if grovepi.ultrasonicRead(ultrasonic_ranger) < 10:
            stop()
            sleep(1)
            servo(180)
            scan_controller.printPosition()
            sleep(1)
            if grovepi.ultrasonicRead(ultrasonic_ranger) > 20:
                servo(125)
                
                print("no be appended")
                enc_tgt(1,1,7)
                
                left_rot()
                
                sleep(2)
                no.append(1)
                
            else:
                sleep (1)
                servo(125)
                sleep(1)
                
                print("no be appened")
                
                enc_tgt(1,1,7)
                right_rot()
                sleep(2)
                no.append(2)
            
                
       
        
        else:
            print ("lol")
            forward()
            sleep(0.1)

            print (grovepi.ultrasonicRead(ultrasonic_ranger))
            
            
    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
    except ValueError:
        print ("Error")
else:
    
              
    print (grovepi.ultrasonicRead(ultrasonic_ranger))
    stop()
    u = raw_input("")
    while grovepi.ultrasonicRead(ultrasonic_ranger) < 300 and len(no) > a:
        print ("while 2 working")
        try:
            if grovepi.ultrasonicRead(ultrasonic_ranger) < 10:
                
                  
                if no[0] == 1:
                    print("right-L")
                    enc_tgt(1,1,7)
                    left_rot()
                    sleep(1)
                    a = a+1
                    print(a)
                else:
                    print("left-L")
                    enc_tgt(1,1,7)
                    right_rot()
                    sleep(1)
                    
                    print(a)
                    a = a+1
                
 
            else:
                forward()
                sleep(0.1)
        except IOError:
            print ("Error")
        except TypeError:
            print ("Error")
    else:
        raw_input("its done")