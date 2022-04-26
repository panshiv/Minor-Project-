from smbus2 import SMBus
from mlx90614 import MLX90614

class TemperatureSensor:
    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = MLX90614(self.bus, address=0x5A)
        #self.bus.close()
    def sense(self):
        #self.bus = SMBus(1)
        #self.sensor = MLX90614(self.bus, address=0x5A)
        temp= self.sensor.get_object_1()
        return temp
'''t1=TemperatureSensor();
while(1):
    x=t1.sense();
    print("temperature ",x);
#print("Ambient Temperature :", sensor.get_ambient())
#print ("Object Temperature :", sensor.get_object_1())
'''