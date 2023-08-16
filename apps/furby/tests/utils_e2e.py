"""
End to end test to check that Raspberry GPIO is properly interfaced
"""

import RPi.GPIO as GPIO
from datetime import datetime
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from furby_utils import BLUE_LED, YELLOW_LED, PHOTO_INPUT, OUTPUT_PINS, init_gpio

def monitor_lightswitch():
    is_on = False
    while(True):
        pin_state = PHOTO_INPUT.is_active
        if pin_state:
            is_on = not is_on
            on_off = "on" if is_on else "off"
            if is_on:
                BLUE_LED.on()
            else:
                BLUE_LED.off()
            print(f"Light turned {on_off} at {datetime.now()}")
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
    monitor_lightswitch()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
