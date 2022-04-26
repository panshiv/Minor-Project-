import RPi.GPIO as GPIO
from time import sleep

class Pump:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        #self.Ena =8
        self.In1=10
        #In2=18

            
        #GPIO.setup(self.Ena,GPIO.OUT)
        GPIO.setup(self.In1,GPIO.OUT)
        #GPIO.setup(In2,GPIO.OUT)
        #self.pwm=GPIO.PWM(self.Ena,100)
        #self.pwm.start(self.Ena)
#print('start')    
    def start_pump(self,x=50,t=0.5):
        GPIO.output(self.In1,GPIO.HIGH)
        print("forward")
        #self.pwm.ChangeDutyCycle(x)
        sleep(t)

    def stop_pump(self):
        GPIO.output(self.In1,GPIO.LOW)
        #self.pwm.ChangeDutyCycle(0)
        print('stop')
'''p=Pump()
p.start_pump()
p.stop_pump()'''
    
