import RPi.GPIO as GPIO
import time
import sys

if len(sys.argv) == 2:
  print(sys.argv[1])

# Setting up something
GPIO.setmode(GPIO.BOARD)

# pins we are playing with
control_pins = [7,11,13,15]

# resetting the pins
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

# Getting the right signals to turn the stepper motor
halfstep_seq_right = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

halfstep_seq_left = [
  [1,0,0,1],
  [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0]
]

# Keeping this as a defaultdirection
halfstep_direction = halfstep_seq_right

if len(sys.argv) == 2:
  print("direction has been added")
  f = open("logger.txt", "a")
  f.write("direction has been added\n")
  f.write("direction is: " + sys.argv[1] + "\n")
  f.close()

  if sys.argv[1] == "right":
    halfstep_direction = halfstep_seq_right
  elif sys.argv[1] == "left":
    halfstep_direction = halfstep_seq_left

# Moving the stepper motor by 32th of a full circle
for i in range(16):
 for halfstep in range(8):
   for pin in range(4):
     GPIO.output(control_pins[pin], halfstep_direction[halfstep][pin])
   time.sleep(0.001)

GPIO.cleanup()
