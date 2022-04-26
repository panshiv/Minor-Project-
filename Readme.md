This  is the code of our minor project titled" Automatic door barrier with face mask destection,temperature scanning and sanitizer deispenser".
Our project includes DC-pump, servo motor, lcd, pi camera, IR- sensor,and temperature sensor(mlx9064).You may connect the circuit and individual modules can be calibrated and checked by running individual modules given.

for pi camera--> run detection.py(it detects facemask)
for lcd--> run lcd.py
for servomotor--> run servo.py ( for using required dutycycle calibrate servo motor by running servotest.py and update values in servo.py before running)
for IR-sensor--> run irsensor.py
for DC-pump--> run pump.py
for Temperature Sensor--> run tempsensor.py

After you are done verifying individual module you can integrate them into a complete system by running main.py.

NOTE: 
    i) You need to uncomment the codes that are commented in end of every code for unit test of modules.
   ii) GPIO PIN used are mentioned in code of individual modules.You may change it as per your requirement.
   iii) The code is applicable in a system with raspberrypi as a processor.
