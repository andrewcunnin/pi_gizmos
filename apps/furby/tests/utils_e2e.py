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
    prev_state = PHOTO_INPUT.is_active
    print(f"Initial state is: {prev_state}")
    for i in range(30):
        pin_state = PHOTO_INPUT.is_active
        if pin_state and not prev_state:
            print(f"Light turned on at {datetime.now()}")
        if prev_state and not pin_state:
            print(f"Light turned off at {datetime.now()}")
        prev_state = pin_state
        time.sleep(1)



def check_outputs():
    for pin in OUTPUT_PINS:
        pin.on()
        print(f"Pin {pin} set to HIGH")
        input("Press ENTER to increment..\n")
        pin.off()
    print("Finished checking pins!")

def main():
    init_gpio()
    # check_outputs()
    monitor_photoresistor()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
