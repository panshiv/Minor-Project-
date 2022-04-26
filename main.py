from lcd import LCD
from servo import Servo
from pump import Pump
from tempsensor import TemperatureSensor
from mask_detection import *
from time import sleep
from irsensor import IRSensor
import RPi.GPIO as GPIO
#from mask_detection import face_mask
#from irsensor import object_detected
#from tempsensor import temp

tempSensor=TemperatureSensor()
#print("value is",tempSensor.sense())

lcd=LCD()
#lcd.print("hello",1)

servoMotor=Servo()
#servoMotor.open()

pump=Pump()
#pump.start_pump()

ir=IRSensor()
#ir.sense()

GPIO.setwarnings(False)
if __name__ == '__main__':
    while True:
        lcd.display("Mask Required",1)
        sleep(5)
        print("Mask Required")
        if(detectMask()):
            print("Check Temperature")
            lcd.display("Wearing Mask",1)
            sleep(2)
            lcd.display("Put your hand",1)
            lcd.display("on sensor",2)
            sleep(2)
            tempet=tempSensor.sense()
            lcd.display("Temperature:",1)
            lcd.display(str(tempet),2)
            sleep(2)
            print(tempet)
            lcd.clear()
            sleep(2)
            if(tempet <= 38 and tempet >=29):
                print("Get Sanitizer")
                lcd.display("Temperature is",1)
                lcd.display("    Normal",2)
                sleep(2)
                lcd.clear()
                lcd.display("Get Sanitizer",1)
                sleep(5)
                if(ir.sense()):
                    pump.start_pump()
                    sleep(0.5)
                    pump.stop_pump()
                    sleep(2)
                    lcd.display("Welcome",1)
                    #servoMotor.close_door()
                    servoMotor.open_door()
                    lcd.display("Door Opened",1)
                    sleep(5)
                    #servoMotor.open_door()
                    servoMotor.close_door()
                    lcd.display("Door Closed",1)
                    sleep(5)
                else:
                    lcd.display("Sanitizer required",1)
                    sleep(5)
            else:
                print("High Temperature")
                lcd.display("Temperature High",1)
                sleep(5)
        else:
            print("Mask Required")
            lcd.display("Mask Required",1)
            sleep(5)

            
