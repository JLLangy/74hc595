import time
import ssd74hc595

# Define GPIO outputs
dataPin  = 11
latchPin = 15
clockPin = 13

# Create object
Display = ssd74hc595.sevenseg(dataPin, latchPin, clockPin)

# Display an eight-character message. Additional characters are truncated.
# Supported characters are 0 - 9, A - Z, [space], -, _
# Lowercase characters are converted to uppercase

Display.Multi("1234ABCD")
