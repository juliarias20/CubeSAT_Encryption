import board
import busio
import time 
import digitalio
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_mcp9600 import MCP9600
import datetime

charBank = " ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890 !@$$%^&*"

#define mosfet pin
mosfet_pin = digitalio.DigitalInOut(board.D13)

#output Mosfet
mosfet_pin.direction = digitalio.Direction.OUTPUT

#incorporate loop to start the encryption process system 
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

cycle = 0
file = open('encryptedFile.txt', 'w')

def caesarianCipher():
      caesarFile = open('passcodes.txt')
      
      for word in caesarFile:
      
          encryptedMessage = ""
      
          lengthOfKey = len(word)
      
          for i in word:
              position = charBank.find(i)
              newPos = position + 5
              encryptedMessage += charBank[newPos]
      
          print("Original word: " + word)
          print("Here is your encrypted code: " + encryptedMessage + "\n")
          time.sleep(5)


while True:

        try:
            #using device i2c register and "k" thermocouple
            e = datetime.datetime.now()
            device = MCP9600(i2c)
            TEMP = ((device.temperature * (9/5))+32)
            file.write("\nCurrent temperature:" + str(TEMP))
            print("First cycle:")
            print("Temperature(F)", (TEMP))
                
            cycle = cycle + 1
                
            time.sleep(1)

            while TEMP < 80:
                #turn mosfet on
                mosfet_pin.value = True
                time.sleep(0.1)  # brief delay to settle
                print("Mosfet ON")
                # wait for 1 sec
                time.sleep(1)
                # re-read temperature
                TEMP = ((device.temperature * (9/5))+32)
                file.write("Current temperature:" + str(TEMP))
                    
                print("Temperature(F)", (TEMP))
                cycle = cycle + 1
                time.sleep(1)

                 # if temperature is 80 or higher, turn mosfet off
                mosfet_pin.value = False
                time.sleep(0.1)  # brief delay to settle
                print("Mosfet OFF")
                file.write(str(TEMP))
                    # wait for 1 sec
                time.sleep(1)

                if(cycle > 5):
                        print("Cycle completed. Encryption running now...")
                        print("The following passcodes are randomized through a file of keywords and will be used for testing purposes.\n")

                        time.sleep(1)

                        caesarianCipher()

        except ValueError:
            print("MCP9600 sensor not detected")
            continue  # skip to the next iteration if sensor not detected



