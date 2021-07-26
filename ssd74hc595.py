# ssd74hc595 -- Library for seven segment displays (ssd) with 74HC595 shift register
# Created to work with boards containing eight seven segment displays
# Author: John-Lee Langford
# Last update: 26-July-2021
# URL: mr.langford.com

import RPi.GPIO as IO
import time

# Ignore warnings
IO.setwarnings(False)

IO.setmode (IO.BOARD)

# Check and normalise display number
def normDisplayIn(displayNumber):
  try:
    dispNo = int(displayNumber)
    # Assume 8-digit display
    if dispNo < 0 or dispNo > 7:
      dispNo = 0
  except:
    dispNo = 0
  return dispNo


# Check and normalise character
def normCharIn(character):
  character = character[0:1]
  character = character.upper()
  return character


# Set display position
position = [
  [0,0,0,0,1,0,0,0], # Position 0 / 8th display
  [0,0,0,0,0,1,0,0], # Position 1 / 7th display
  [0,0,0,0,0,0,1,0], # Position 2 / 6th display
  [0,0,0,0,0,0,0,1], # Position 3 / 5th display
  [1,0,0,0,0,0,0,0], # Position 4 / 4th display
  [0,1,0,0,0,0,0,0], # Position 5 / 3rd display
  [0,0,1,0,0,0,0,0], # Position 6 / 2nd display
  [0,0,0,1,0,0,0,0]  # Position 7 / 1st display
]

# Set segments to light
segments = {
  "0": [1,1,0,0,0,0,0,0],
  "1": [1,1,1,1,1,0,0,1],
  "2": [1,0,1,0,0,1,0,0],
  "3": [1,0,1,1,0,0,0,0],
  "4": [1,0,0,1,1,0,0,1],
  "5": [1,0,0,1,0,0,1,0],
  "6": [1,0,0,0,0,0,1,0],
  "7": [1,1,1,1,1,0,0,0],
  "8": [1,0,0,0,0,0,0,0],
  "9": [1,0,0,1,0,0,0,0],
  "A": [1,0,0,0,1,0,0,0],
  "B": [1,0,0,0,0,0,1,1],
  "C": [1,1,0,0,0,1,1,0],
  "D": [1,0,1,0,0,0,0,1],
  "E": [1,0,0,0,0,1,1,0],
  "F": [1,0,0,0,1,1,1,0],
  "G": [1,1,0,0,0,0,1,0],
  "H": [1,0,0,0,1,0,0,1],
  "I": [1,1,0,0,1,1,1,1],
  "J": [1,1,1,1,0,0,0,1],
  "K": [1,0,0,0,1,0,1,0],
  "L": [1,1,0,0,0,1,1,1],
  "M": [1,1,0,1,0,1,0,0],
  "N": [1,1,0,0,1,0,0,0],
  "O": [1,1,0,0,0,0,0,0],
  "P": [1,0,0,0,1,1,0,0],
  "Q": [1,0,0,1,1,0,0,0],
  "R": [1,1,0,0,1,1,1,0],
  "S": [1,0,0,1,0,0,1,0],
  "T": [1,0,0,0,0,1,1,1],
  "U": [1,1,0,0,0,0,0,1],
  "V": [1,1,0,1,0,0,0,1],
  "W": [1,1,1,0,0,0,1,0],
  "X": [1,0,1,1,0,1,1,0],
  "Y": [1,0,0,1,0,0,0,1],
  "Z": [1,0,1,0,0,1,0,0],
  " ": [1,1,1,1,1,1,1,1],
  "-": [1,0,1,1,1,1,1,1],
  "_": [1,1,1,1,0,1,1,1]
}

class sevenseg:
  __dPin = 0
  __lPin = 0
  __cPin = 0

  def __init__(self, dataPin, latchPin, clockPin):
    self.__dPin = dataPin
    self.__lPin = latchPin
    self.__cPin = clockPin
    IO.setup(self.__dPin, IO.OUT)
    IO.setup(self.__lPin, IO.OUT)
    IO.setup(self.__cPin, IO.OUT)
  # end  __init__


  def Single(self, charIn, displayIn, dPoint):
    charIn = str(charIn)
    charIn = normCharIn(charIn)
    displayIn = normDisplayIn(displayIn)

    displayData = segments.get(charIn, [1,1,1,1,1,1,1,1]) + position[int(displayIn)]

    # Check for decimal point
    if dPoint:
      displayData[0] = 0

    IO.output(self.__lPin, 0)
    for i in range(0, 16):
      IO.output(self.__cPin, 0)
      IO.output(self.__dPin, displayData[i])
      IO.output(self.__cPin, 1)
    IO.output(self.__lPin, 1)



  def Multi(self, textIn):
    # Ensure data is 8 characters long
    if len(textIn) > 8:
      textIn = textIn[0:8]
    while len(textIn) < 8:
      textIn = " " + textIn

    #for x in range(0, 8):
    #  textOut = normCharIn(textIn[x])

    textIn = textIn [::-1]

    textIn = textIn.upper()

    # Populate displayData
    displayData = [[],[],[],[],[],[],[],[]]
    for x in range(0,8):
      displayData[x] = segments.get(textIn[x], [1,1,1,1,1,1,1,1]) + position[int(x)]

    while True:
      for j in range(0,8):
        IO.output(self.__lPin, 0)
        for i in range(0,16):
          IO.output(self.__cPin, 0)
          IO.output(self.__dPin, displayData[j][i])
          IO.output(self.__cPin, 1)

        IO.output(self.__lPin, 1)
