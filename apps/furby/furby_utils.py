import logging
from gpiozero import LED, InputDevice
import RPi.GPIO as GPIO

# OUTPUTS
BLUE_LED = LED(13)
YELLOW_LED = LED(7)

OUTPUT_PINS = [BLUE_LED, YELLOW_LED]


# INPUTS
PHOTO_INPUT = InputDevice(21)

INPUT_PINS = [PHOTO_INPUT]

init_gpio():
    GPIO.setmode(GPIO.BCM)
