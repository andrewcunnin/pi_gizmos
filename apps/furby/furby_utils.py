import logging
from gpiozero import LED, InputDevice
# OUTPUTS
BLUE_LED = LED(13)
YELLOW_LED = LED(7)

OUTPUT_PINS = [BLUE_LED, YELLOW_LED]


# INPUTS
PHOTO_INPUT = InputDevice(21)

INPUT_PINS = [PHOTO_INPUT]

GPIO.setmode(GPIO.BCM)
for pin in OUTPUT_PINS:
    GPIO.setup(pin, GPIO.OUT)
for pin in INPUT_PINS:
    GPIO.setup(pin, GPIO.IN)
