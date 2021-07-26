# Example of displaying a counter on
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

counter = 0
while True:

  counterStr = str(counter)

  # If the number is less than 8 digits, populate the missing numbers with spaces
  while len(counterStr) < 8:
    counterStr = " " + counterStr

  # Reverse number
  counterStr = counterStr [::-1]

  # Cycle through displays 2000 times
  for x in range(2000):
    for i in range(8):
      Display.Single(counterStr[i], i, False)

  counter = counter + 1
