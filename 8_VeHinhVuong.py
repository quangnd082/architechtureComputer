import time
import Adafruit_Nokia_LCD as LCD 
 
from PIL import Image 
from PIL import ImageDraw 
def main():
     
    SCLK = 23 
    DIN = 27 
    DC = 17 
    RST = 15 
    CS = 18 
    global disp 
    disp = LCD.PCD8544 (DC, RST, SCLK, DIN, CS) 
    disp.begin (contrast=50) 
     
    disp.clear() 
    disp.display()  
    image = Image.new('1', (LCD.LCDWIDTH, LCD. LCDHEIGHT)) 
     
    draw = ImageDraw.Draw(image) 
    draw.rectangle ((22,4, 62, 44), outline=0, fill=255) 
        
    disp.image(image) 
    disp.display () 
    while True:
        time.sleep(2) 
try:
    main() 
except KeyboardInterrupt: 
    disp.clear()

