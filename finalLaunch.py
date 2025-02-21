import board
import busio
import time 
import digitalio
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_mcp9600 import MCP9600
import datetime
import serial
import random

# ---------- VARIABLES -----------

# DATE AND TIME VARIABLES
now = datetime.datetime.now()
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# CHAR BANK + ENCRYPTION ALGORITHM VARIABLES
charBank = " ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890 !@$$%^&*"
cycle = 0
file = open('encryptedFile.txt', 'w')

# MOSFET + I2C VARIABLES
mosfet_pin = digitalio.DigitalInOut(board.D13)

mosfet_pin.direction = digitalio.Direction.OUTPUT

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

ser = serial.Serial ("/dev/ttyS0", 9600)


# --------- ENCRYPTION ALGORITHM ---------
def caesarianCipher():
    caesarFile = open('passcodes.txt')
    
    for word in caesarFile:
    
        encryptedMessage = ""

        lengthOfKey = len(word)

        for i in word:
            position = charBank.find(i)
            newPos = position + 5
            encryptedMessage += charBank[newPos]


    #Terminal Testing
    print("Original word: " + word)
    #ser.write("Original word: " + word)

    print("Here is your encrypted code: " + encryptedMessage + "\n")
    #ser.write("Here is your encrypted code: " + encryptedMessage + "\n")
    time.sleep(1)

# --------- MOSFET ON ALGORITHM ----------
def mosfetON():
    
    file = open('encryptedFile.txt', 'w')
    cycle = 0
    # Set MOSFET Pin value to TRUE --- print output to terminal
    mosfet_pin.value = True
    time.sleep(0.1)
    
    #SEND TO UART ---
    print("Mosfet ON")
    #ser.write("Mosfet ON")

    time.sleep(1)

    # Re-read temperature and print output to device file
    TEMP = ((device.temperature * (9/5))+32)
    file.write(formatted_datetime + "--- Current temperature:" + str(TEMP) + "\n")

	    # Increase the cycle number
    while(cycle < 5):  
        cycle += 1

        #Send to UART and terminal--
        print("CYCLE NUMBER: " + str(cycle))
        print("Temperature(F)", (TEMP))

        #ser.write("CYCLE NUMBER: " + cycle)
        #ser.write("Temperature(F)", (TEMP))

        time.sleep(1)

    if(cycle == 5):

        # Send to UART ----- 

        print("Cycle completed. Encryption running now...")
        print("The following passwords are randomized through a file of keywords and will be used for testing purposes.\n")

        #ser.write("Cycle completed. Encryption running now...")
        #ser.write("The following passwords are randomized through a file of keywords and will be used for testing purposes.\n")

        time.sleep(1)

        #Output randomized passwords and their encrypted code --- demonstrate encryption algorithm.
        caesarianCipher()

        with open("passcodes.txt", 'r') as file:
            password = file.read().splitlines()
            word = password[random.randint(0,100)]

        def encrypt(word):
            finalMessage = ""
            lengthOfKey = len(word)

            for i in word:
                position = charBank.find(i)
                newPos = position + 5
                finalMessage += charBank[newPos]

            return finalMessage;

        #Inform the user of their password for the file.
        print("Your password is: " + word)
        #ser.write("Your password is: " + word)

        #Establish the encryption code for the password and print the encrypted code to the user.
        attempt = encrypt(word)

        print("The encrypted code is: " + attempt)
        #ser.write("The encrypted code is: " + attempt)

        attemptedMessage = ""

        isMessageAccepted = False

        # cesarian cipher algorithm
        for i in attempt:
            position = charBank.find(i)
            newPos = position - 5
            attemptedMessage += charBank[newPos]

        if(attemptedMessage == word):
            isMessageAccepted == True;

            print("Message accepted! File transferred!")
            #ser.write("Message accepted! File transferred!")

            time.sleep(2)

            print("Opening file...")
            #ser.write("Opening file...")

            time.sleep(2)

            file = open('encryptedFile.txt', 'r')

            print(file.read())
            #ser.write(file.read())

# --------- MOSFET OFF ALGORITHM ---------
def mosfetOFF():
    
    file = open('encryptedFile.txt', 'w')
    cycle = 0
    #If temperature is greater than 80, turn MOSFET off
    mosfet_pin.value = False
    time.sleep(0.1)  # brief delay to settle
    
    # Send to UART and terminal --- 
    print("MOSFET OFF")
    #ser.write("Mosfet OFF")

    # Write the current temperature to device file
    file.write(formatted_datetime + "--- Current temperature:" + str(TEMP) + "\n")

    while(cycle < 5):  
        cycle += 1

    	#Send to UART and terminal--
        print("CYCLE NUMBER: " + str(cycle))
        print("Temperature(F)", (TEMP))

    	#ser.write("CYCLE NUMBER: " + cycle)
    	#ser.write("Temperature(F)", (TEMP))
	
        time.sleep(1)
    
    if(cycle == 5):

        # Send to UART ----- 

        print("Cycle completed. Encryption running now...")
        print("The following passwords are randomized through a file of keywords and will be used for testing purposes.\n")

        #ser.write("Cycle completed. Encryption running now...")
        #ser.write("The following passwords are randomized through a file of keywords and will be used for testing purposes.\n")

        time.sleep(1)

        #Output randomized passwords and their encrypted code --- demonstrate encryption algorithm.
        caesarianCipher()

        with open("passcodes.txt", 'r') as file:
            password = file.read().splitlines()
            word = password[random.randint(0,100)]

        def encrypt(word):
            finalMessage = ""
            lengthOfKey = len(word)

            for i in word:
                position = charBank.find(i)
                newPos = position + 5
                finalMessage += charBank[newPos]

            return finalMessage;

        #Inform the user of their password for the file.
        print("Your password is: " + word)
        #ser.write("Your password is: " + word)

        #Establish the encryption code for the password and print the encrypted code to the user.
        attempt = encrypt(word)

        print("The encrypted code is: " + attempt)
        #ser.write("The encrypted code is: " + attempt)

        attemptedMessage = ""

        isMessageAccepted = False

        # cesarian cipher algorithm
        for i in attempt:
            position = charBank.find(i)
            newPos = position - 5
            attemptedMessage += charBank[newPos]

        if(attemptedMessage == word):
            isMessageAccepted == True;

            print("Message accepted! File transferred!")
            #ser.write("Message accepted! File transferred!")

            time.sleep(2)

            print("Opening file...")
            #ser.write("Opening file...")

            time.sleep(2)

            file = open('encryptedFile.txt', 'r')

            print(file.read())
            #ser.write(file.read())

# ---------- LAUNCHING ALGORITHM ---------
while True:
    try:
        # Establish variables for date and time + Write current temperature to the device file.
        e = datetime.datetime.now()
        device = MCP9600(i2c)
        TEMP = ((device.temperature * (9/5))+32)
        file.write(formatted_datetime + "--- Current temperature:" + str(TEMP) + "\n")

        # Check the device temperature and turn on MOSFET accordingly
        while(TEMP < 60):
            mosfetOn()

        while(TEMP > 75):
            mosfetOFF()


    except ValueError:
        print("MCP 9600 not detected.")
            #ser.write("MCP	9600 sensor not detected")








