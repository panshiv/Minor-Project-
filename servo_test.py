import RPi.GPIO as GPIO
from time import sleep
control = [10,9.5,9,8.5,8,7.5,7,6.5,6,5.5,5]
control2 =[5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(22,50) # GPIO 22 for PWM with 50Hz
#In1=22
p.start(2.5) # Initialization
#GPIO.setup(In1,GPIO.OUT)
def open_door():
    for i in range(11):
        print(control[i])
        p.ChangeDutyCycle(control[i])
    print("open")
    p.ChangeDutyCycle(0)
def close_door():
    for i in range(11):
        print(control[i])
        p.ChangeDutyCycle(control2[i])
    print("close")


try:
    while True:
        '''for x in range(11):
            p.ChangeDutyCycle(control[x])
            sleep(1)
            print(x)
            
        for x in range(9,0,-1):
            p.ChangeDutyCycle(control[x])
            sleep(1)
            print(x)
        
        p.ChangeDutyCycle(5.5)
        sleep(2)
        p.ChangeDutyCycle(8.5)
        sleep(2)
        open_door()
        sleep(2)
        close_door()
        '''
        

except KeyboardInterrupt:
    GPIO.cleanup()
    
GPIO.cleanup()