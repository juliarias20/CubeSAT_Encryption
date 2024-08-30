import board
import busio
import time
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_mcp9600 import MCP9600




i2c= busio.I2C(board.SCL,board.SDA, frequency=100000)
while True:
    try:
        #using device i2c register and "k" thermocouple
        device = MCP9600(i2c)
        print("Temperature(F)",((device.temperature * (9/5))+32))
        time.sleep(1)
    except ValueError:
        print("MCP9600 sensor not detected")