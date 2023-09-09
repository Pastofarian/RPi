import RPi.GPIO as GPIO   ## Import GPIO Library
import time               ## Import the time library
 
inPin = 8                 ## Switch connected to pin 8
GPIO.setwarnings(False)     ## Disable warnings
GPIO.setmode(GPIO.BOARD)    ## Use BOARD pin numbering
GPIO.setup(inPin, GPIO.IN)  ## Set pin 8 to INPUT
 
while True:                 
    value = GPIO.input(inPin) ## Read input from switch
    print(value)
    if value:                 ## If switch is pressed
        print ("Pressed")
    else:                     ## Else switch is released
        print ("Not Pressed")
    time.sleep(0.1)           ## the delay is needed for the Raspberry Pi 4 because of its cpu speed
GPIO.cleanup() 

#time.sleep(0.1) introduces a delay of 0.1 seconds in each iteration of the loop. This delay is useful to prevent the script from continuously polling the GPIO pin at the maximum possible rate, which would unnecessarily load the CPU.
# We tu:wqrn off warnings because we will quit with ctr + C so the instruction will never really be finished
