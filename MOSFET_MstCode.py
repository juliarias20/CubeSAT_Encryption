import digitalio
import board
import time

#define mosfet pin
mosfet_pin= digitalio.DigitalInOut(board.D13)

#output Mosfet
mosfet_pin.direction=digitalio.Direction.OUTPUT

while True:
    #turn mosfet on
    mosfet_pin.value=True
    print("Mosfet ON")
    #waite for 1 sec
    time.sleep(1)
    
    #turn off Mosfet
    mosfet_pin.value=False