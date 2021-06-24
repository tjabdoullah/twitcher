import RPi.GPIO as GPIO
import time
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

# Moving the stepper motor by 32th of a full circle
for i in range(16):
 for halfstep in range(8):
   for pin in range(4):
     GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
   time.sleep(0.001)

GPIO.cleanup()
