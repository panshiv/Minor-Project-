import RPi.GPIO as GPIO
from time import sleep

class Servo:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(22,GPIO.OUT)
        GPIO.setwarnings(False)
        self.p = GPIO.PWM(22,50) # GPIO 25 for PWM with 50Hz
        self.p.start(2.5) # Initialization
    def open_door(self):
        self.p.ChangeDutyCycle(8.5)#right 90
        sleep(1)
        print('open')
        #p.ChangeDutyCycle(0)
        #p.stop()
    def close_door(self):  
        self.p.ChangeDutyCycle(5.5)#left_90
        sleep(0.5)
        print('close')
'''test=Servo()
while True:
    
    test.open_door()
    sleep(2)
    test.close_door()
    sleep(2)
'''
