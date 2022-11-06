# viet chuong trinh hien thi khoang cach > 10 RED SANG, <10 RED tat

import RPi.GPIO as GPIO
import time
import Adafruit_Nokia_LCD as LCD
from PIL import Image, ImageDraw, ImageFont

def main() :
    TRIG = 16
    ECHO = 26
    LED1 = 13
    LED2 = 19

    global pulse_end
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.output(TRIG, False)

    while True :
            print('Distance measurement in progress...')
            time.sleep(2)
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()
            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()
            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            if distance > 10 :
                GPIO.output(LED1, GPIO.HIGH)
                GPIO.output(LED2, GPIO.LOW)
            else:
                GPIO.output(LED1, GPIO.LOW)
                GPIO.output(LED2, GPIO.HIGH)


try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    
