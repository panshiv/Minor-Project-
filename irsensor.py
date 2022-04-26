import RPi.GPIO as GPIO
import time

class IRSensor:
    def __init__(self):
        self.sensor = 8
        #buzzer = 18

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sensor,GPIO.IN)
        #GPIO.setup(buzzer,GPIO.OUT)
    def sense(self):
        return not(GPIO.input(self.sensor))

#GPIO.output(buzzer,False)
#print ("IR Sensor Ready.....")
#print (" ")
'''
try: 
   while True:
      if (GPIO.input(sensor)== False):
          #GPIO.output(buzzer,True)
          Object_detected=1
          print ("Object Detected")
          while GPIO.input(sensor):
              time.sleep(0.5)
      else:
          #GPIO.output(buzzer,False)
          print("object is not detected")
except KeyboardInterrupt:
    GPIO.cleanup()
'''