import RPi.GPIO as GPIO
import time

def main():

    BT1 = 14
    LED = 22
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)
    ispressBT1 = False
   
    while True:
        if GPIO.input(BT1) == GPIO.LOW:  
            print("BT1 press")
        
            if ispressBT1:
                GPIO.output(LED, GPIO.LOW)
                ispressBT1 = False
                time.sleep(0.3)
                continue
            if not ispressBT1:
                GPIO.output(LED, GPIO.HIGH)
                ispressBT1 = True
                time.sleep(0.3)
                continue
try:
    main()  
except KeyboardInterrupt:  
    GPIO.cleanup()  