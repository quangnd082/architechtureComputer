import RPi.GPIO as GPIO
import time
import Adafruit_Nokia_LCD as LCD
from PIL import Image, ImageDraw, ImageFont

def main():
    BT1 = 14
    TRIG = 16
    ECHO = 26
    global pulse_end
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)

    while True:
        if GPIO.input(BT1) == 0:
            print("Waiting for sensor to settle")
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
            lcd(distance)
            if distance > 100:
                print("Error, try again")
            else:
                print("Distance:", distance, "cm")
            time.sleep(1)


def lcd(distance):
    SCLK = 23
    DIN = 27
    DC = 17
    RST = 15
    CS = 18
    global disp
    disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
    disp.begin(contrast=60)
    disp.clear()
    disp.display()
    image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, LCD.LCDWIDTH-1, LCD.LCDHEIGHT-1),
                   outline=0, fill=255)
    font = ImageFont.load_default()
    draw.text((10, 3),'Dist:'+str(distance)+'cm',font=font)
    disp.image(image)
    disp.display()

try:
    main()
except KeyboardInterrupt:
    print("----Program stopped by User----")
    GPIO.cleanup()
