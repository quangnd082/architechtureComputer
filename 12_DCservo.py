import RPi.GPIO as GPIO
import time
def main():
    BT1 = 14
    BT2 = 4     # Khởi tạo các nút bấm
    BT3 = 3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Cài đặt các nút bấm và pull_up chúng
    GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global s    # Khởi tạo biến global
    s = sg90()

    anglepulseBT1 = 5   # Khởi tạo góc quay mỗi lần bấm của servo là 5 độ 

    print("Tat ca da san sang")
    while True:
        if GPIO.input(BT1) == GPIO.LOW: # Nếu ta bấm nút BT1 thì in ra dòng chữ quay 5 độ,đồng thời servo quay 5 độ 
            print("quay 5 angle")
            anglepulseBT1 = controlservo(s, anglepulseBT1)
def controlservo(s, anglepulseBT):
    current  = s.currentdirection()
    if current >=180 or current <= 0:
        anglepulseBT = -anglepulseBT
    rotato = anglepulseBT + current
    rotato = 180 if rotato >= 180 else 0 if rotato <= 0 else rotato
    s.setdirection(rotato, 40)
    time.sleep(0.5)
    return anglepulseBT

class sg90:
    def __init__(self):
        self.pin = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0.0)
        self.direction = 90
    def cleanup(self):
        self.servo.ChangeDutyCycle(self._henkan(0))
        time.sleep(0.3)
        self.servo.stop()
        GPIO.cleanup()
    def currentdirection(self):
        return self.direction
    def _henkan(self, value):
        return round(0.056 * value + 2.0)
    def setdirection(self, direction, speed):
        for d in range(self.direction, direction, int(speed)):
            self.servo.ChangeDutyCycle(self._henkan(d))
            self.direction = d
            time.sleep(0.1)
        self.servo.ChangeDutyCycle(self._henkan(direction))
        self.direction = direction
try:
    main()
except KeyboardInterrupt:
    s.cleanup()





