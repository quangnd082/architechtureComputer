# viet chuong trinh lan 1 RED sang, lan 2 RED tat

import RPi.GPIO as GPIO

BT1 = 4
LED1 = 22
dem = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED1, GPIO.OUT)

while True :
    if GPIO.input(BT1) == GPIO.LOW :
        dem = dem + 1
        if dem == 1 :
            GPIO.output(LED1, GPIO.HIGH)
        if dem == 2 :
            GPIO.output(LED1, GPIO.LOW)
        if dem > 2 :
            dem = 0
