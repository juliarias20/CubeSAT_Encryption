import board
import busio
import time
import digitalio
import time

from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_mcp9600 import MCP9600

#define mosfet pin
mosfet_pin= digitalio.DigitalInOut(board.D13)

#output Mosfet
mosfet_pin.direction=digitalio.Direction.OUTPUT

tempFile = open("temperatureReadings.txt", "w")

i2c= busio.I2C(board.SCL,board.SDA, frequency=100000)
while True:
    try:
        #using device i2c register and "k" thermocouple
        device = MCP9600(i2c)
        TEMP=((device.temperature * (9/5))+32)
        print("Temperature(F)",(TEMP))
        tempFile.write(TEMP + "\n")
        
        time.sleep(1)
    except ValueError:
        print("MCP9600 sensor not detected")
        
    if TEMP<80:
        #turn mosfet on
        mosfet_pin.value=True
        print("Mosfet ON")
        #waite for 1 sec
        time.sleep(1)
    else:
        #turn mosfet on
        mosfet_pin.value=True
        print("Mosfet ON")
        #waite for 1 sec
        time.sleep(1)
        
