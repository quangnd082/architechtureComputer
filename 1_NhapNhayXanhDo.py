#viet chuong trinh bam BT1 tat het den
import RPi.GPIO as GPIO
import time
def main():
    BT1 = 14
    LED1 = 22
    LED2 = 27

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    
    while True:
        if GPIO.input(LED1) == GPIO.LOW:
            GPIO.output(LED1, GPIO.HIGH)
            GPIO.output(LED2, GPIO.LOW)

            if GPIO.input(BT1) == GPIO.LOW:
                GPIO.output(LED1, GPIO.LOW)
                print("BT1 press")
                break
            time.sleep(1)

        if GPIO.input(LED2) == GPIO.LOW:
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.HIGH)
            if GPIO.input(BT1) == GPIO.LOW:
                GPIO.output(LED2, GPIO.LOW)
                print("BT1 press")
                break
            time.sleep(1)
try:
    main()
except KeyboardInterupt:
    GPIO.cleanup()