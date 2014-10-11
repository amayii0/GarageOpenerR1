# Original source code taken from
#   Raspberry Pi control from mobile device or desktop web browser 
#   http://electronicsbyexamples.blogspot.be/2014/02/raspberry-pi-control-from-mobile-device.html

import RPi.GPIO as GPIO
import time

# BCM to WiringPi pin numbers
PIN_RELAYCMD    = 17 # Relay command pin
PIN_OPENSWITCH  = 18 # Button pin - Open state
PIN_CLOSESWITCH = 27 # Button pin - Closed state

def Init():
    GPIO.setwarnings(False) # suppress GPIO used message
    GPIO.setmode(GPIO.BCM) # use BCM pin numbers
    GPIO.setup(PIN_RELAYCMD, GPIO.OUT) # set LED pin as output

    # set button pin as input and use internal pull-up so we don't need external resistor
    GPIO.setup(PIN_OPENSWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PIN_CLOSESWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ShortSwitch():
    print "Sending ShortSwitch to pin {0}".format(PIN_RELAYCMD)
    GPIO.output(PIN_RELAYCMD, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(PIN_RELAYCMD, GPIO.LOW)
    
def ReadDoorState():
    # Open state   =  1
    # Closed state =  0
    # States error = -1
    # Intermediate = -2
    # Script error = -3
    openState   = ReadOpenSwitch() 
    closedState = ReadClosedSwitch()
    
    if (openState and closedState):
      return -1 # Both are true, this would mean door is opened and closed at the same time
    elif (openState==False) and (closedState==False):
      return -2 # Both are false, this mean door is neither opened or closed, so assume half way (moving or stopped!)
    elif (openState):
      return 1 # Open switch
    elif (closedState):
      return 0 # Close switch
    else:  
      return -3 # Unknown error, this should never occur. If it does there's a bug in the previous tests

def ReadOpenSwitch():
    return ReadSwitch(PIN_OPENSWITCH)

def ReadClosedSwitch():
    return ReadSwitch(PIN_CLOSESWITCH)

def ReadSwitch(sPin):
    return GPIO.input(sPin) == 0
