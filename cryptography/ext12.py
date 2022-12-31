import string as s 

# Global variables
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""
lettersLower = s.ascii_lowercase
lettersUpper = s.ascii_uppercase
numbers = s.digits
symbols = s.punctuation
possibleCharacters = lettersLower + lettersUpper + numbers + symbols
runProgram = 'yes'
# Define the function called encryptOrDecrypt
def encryptOrDecrypt():
  global shiftedPosition  
  if mode.lower() == "encrypt":
    shiftedPosition = initialPosition + key
  elif mode.lower() == "decrypt":
    shiftedPosition = initialPosition - key

# Define the function called wraparound
def wrapAround():
  global shiftedPosition
  if shiftedPosition >= len(possibleCharacters):
      shiftedPosition = shiftedPosition - len(possibleCharacters)
  elif shiftedPosition < 0:
    shiftedPosition = shiftedPosition + len(possibleCharacters)
# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\n\nLet's get started!\n")

# Receive user input
while runProgram == 'yes':
  initialMessage = input("What is your message? ")
  key = int(input("What is the key? Choose a number from 0 to 93. "))
  mode = input("Do you want to encrypt or decrypt? ")
  
  # Encrypt or decrypt the message
  for character in initialMessage:
    if character in possibleCharacters:
      initialPosition = possibleCharacters.find(character)
  
      encryptOrDecrypt()
      wrapAround()
  
      shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
    
    else:
      shiftedMessage = shiftedMessage + character
  
  # Print the shifted message
  if mode.lower() == 'encrypt' or mode.lower() == 'decrypt':
    print("Your " + mode.lower() + "ed message is: " + shiftedMessage)
    runProgram = input("Do you want to encrypt or decrypt another message? Type yes or no. ")
  print("\n")
  shiftedMessage = ""
  else:
    print("Try again, and make sure you either type 'encrypt' or 'decrypt.'")