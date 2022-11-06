import RPi.GPIO as GPIO
import time
import Adafruit_Nokia_LCD as LCD
from PIL import Image, ImageDraw, ImageFont

BT1 = 4
SCLK = 23
DIN = 27
DC = 17
RST = 15
CS = 19

dem = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

global disp
disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)
disp.begin(contrast=80)
disp.clear()
disp.display()
image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
font = ImageFont.load_default()

mess = '   Hello World   '
mess = list(mess)
def run(n) :
    k = n[len(n)-1]
    for i in range(len(n)-1,-1,-1) :
         n[i] = n[i-1]
    n[0] = k
    return n

def toString(n) : 
    s = ''
    for i in n :
        s += i
    return s

while True :
    if GPIO.input(BT1) == GPIO.LOW :
        dem = 1

    if dem == 1 :
        disp.clear()
        mess = run(mess)
        draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
        draw.text((8,30), toString(mess), font=font)
        draw.line((0,31,84,31), fill=0)
        disp.image(image)
        disp.display()
    time.sleep(0.01)
    