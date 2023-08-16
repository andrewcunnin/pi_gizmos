"""
End to end test to check that Raspberry GPIO is properly interfaced
"""

import RPi.GPIO as GPIO
from datetime import datetime
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from furby_utils import BLUE_LED, YELLOW_LED, PHOTO_INPUT, OUTPUT_PINS

def monitor_photoresistor():
    for i in range(10):
        print(PHOTO_INPUT.active_state())
        time.sleep(1)



def check_outputs():
    for pin in OUTPUT_PINS:
        pin.on()
        print(f"Pin {pin} set to HIGH")
        input("Press ENTER to increment..\n")
        pin.off()
    print("Finished checking pins!")

def main():
    check_outputs()
    monitor_photoresistor()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
