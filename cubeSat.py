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

#incorporate loop to start the encryption process system 
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

cycle = 0
file = open('encryptedFile.txt', 'w')

while True:
    while (cycle < 0):


        try:
            #using device i2c register and "k" thermocouple
            device = MCP9600(i2c)
            TEMP = ((device.temperature * (9/5))+32)
            file.write(TEMP)
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
                file.write(TEMP)
                print("Temperature(F)", (TEMP))
                time.sleep(1)

            # if temperature is 80 or higher, turn mosfet off
            mosfet_pin.value = False
            time.sleep(0.1)  # brief delay to settle
            print("Mosfet OFF")
            file.write(TEMP)
            # wait for 1 sec
            time.sleep(1)
        except Exception as e:

            print("Error:", e)

        cycle = cycle + 1

userInput = input('Please input a sentence to encrypt: ')


#char bank to obtain letters from
charBank = " ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890 !@$$%^&*"

#holding message
encryptedMessage = ""

lengthOfKey = len(userInput)

#a for loop which takes the current position in the userInput and changes it to the encrypted message
for i in userInput:
    position = charBank.find(i)
    newPos = position + 5
    encryptedMessage += charBank[newPos]

time.sleep(1)

print("Here is your encrypted code: " + encryptedMessage)


time.sleep(1)

#verification process
attemptedMessage = ""
attempt = input("What is the passcode? ")

isMessageAccepted = False

for i in attempt:
    position = charBank.find(i)
    newPos = position + 5
    attemptedMessage += charBank[newPos]

while(isMessageAccepted == False):
    if(attemptedMessage == encryptedMessage):
        isMessageAccepted == True;
        print("Message accepted! File transferred!")
        time.sleep(2)
        print("Opening file...")
        time.sleep(2)
        file = open('encryptedFile.txt', 'r')
        print(file.read())

    else:
        print("Message not accepted.")



    
