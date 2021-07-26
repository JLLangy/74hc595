# Example of displaying eight-digit random numbers using
# 8 x seven-segment displays controlled by 74HC595 shift register
# Author: John-Lee Langford
# Last update: 26-July-2021
# URL: mr.langford.com

import time
import ssd74hc595
import random

# Define GPIO outputs
dataPin  = 11
latchPin = 15
clockPin = 13

# Create object
Display = ssd74hc595.sevenseg(dataPin, latchPin, clockPin)

# Display a single character in on a specific display and repeat to build-up an eight character output
# Useage: Display.Single(character [int / str], displayNumber [0 - 9], decimal point [True / False])
# Note: display 0 is on the right of the board

while True:
  # Pick a random number
  randomNumber = str(random.randint(0, 99999999))

  # If the number is less than 8 digits, populate the missing numbers with spaces
  while len(randomNumber) < 8:
    randomNumber = " " + randomNumber

  # Reverse number
  randomNumber = randomNumber [::-1]

  # Cycle through displays 2000 times
  for x in range(2000):
    for i in range(8):
      Display.Single(randomNumber[i], i, False)
