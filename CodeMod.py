import board
import busio
import time
import digitalio
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_mcp9600 import MCP9600

#define mosfet pin
mosfet_pin = digitalio.DigitalInOut(board.D13)

#output Mosfet
mosfet_pin.direction = digitalio.Direction.OUTPUT

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

while True:
    try:
        #using device i2c register and "k" thermocouple
        device = MCP9600(i2c)
        TEMP = ((device.temperature * (9/5))+32)
        print("Temperature(F)", (TEMP))
        time.sleep(1)
    except ValueError:
        print("MCP9600 sensor not detected")
        continue  # skip to the next iteration if sensor not detected

    try:
        while TEMP < 80:
            #turn mosfet on
            mosfet_pin.value = True
            time.sleep(0.1)  # brief delay to settle
            print("Mosfet ON")
            # wait for 1 sec
            time.sleep(1)
            # re-read temperature
            TEMP = ((device.temperature * (9/5))+32)
            print("Temperature(F)", (TEMP))
            time.sleep(1)

        # if temperature is 80 or higher, turn mosfet off
        mosfet_pin.value = False
        time.sleep(0.1)  # brief delay to settle
        print("Mosfet OFF")
        # wait for 1 sec
        time.sleep(1)
    except Exception as e:
        print("Error:", e)