import time
from datetime import datetime

""" Pseudocode:
GOAL: to successfully encrypt a file that can be opened with a passcode. 

1. create a file that can be encrypted
2. create an option to choose to encrypt the file. 
3. encrypt the file
4. choose to open the file with a passcode
5. choose passcode
6.set passcode to file


"""

""" During the project, any temperature reading would be transported onto the file itself.
    After encrypting the file with a key, we will use this message to unlock  and lock the file back and forth.
    Potential research purposes include: using radio frequency to hack the process, UI system development
    Questions: can we transport this file from the pi to our ground station? 
"""

charBank = " ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890 !@$$%^&*"

tempfile = open('encryptedFile.txt', 'w')

tempfile.write("These are today's temperature data readings:  \n")

temperature = 0

while((temperature >= 0) & (temperature < 78)):
    temperature = temperature + 3.5;
    tempfile.write('Temperature: %s\n' %temperature)

tempfile.close()

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

        #time.sleep(5)

def vingenereCipher():
    file = open("passcodes.txt", "r")
    keywordFile = open("keywords.txt", "r")

    for word in file:
        passcode = word
        key = "hello"

        def convertToCipher(password, key):
            cipher = ""
            for i in password:
                x = ((password.find(i) + key.find(i)) % 26)

                x += ord('A')
                cipher += chr(x)
        return cipher

    print("Original word: " + word)
    print("Here is your encrypted code: " + caesarianCipher(passcode, key) + "\n")


#introduction Message
print("The following passcodes are randomized through a file of keywords and will be used for testing purposes.\n")

time.sleep(1)

caesarianCipher()

time.sleep(1)

#verification process
attemptedMessage = ""
attempt = input("What is the passcode? ")

isMessageAccepted = False


# cesarian cipher algorithm
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

