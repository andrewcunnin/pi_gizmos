"""
End to end test to check that Raspberry GPIO is properly interfaced
"""

import RPi.GPIO as GPIO
from datetime import datetime
import time
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from furby_utils import BLUE_LED, YELLOW_LED, PHOTO_INPUT

def monitor_photoresistor():
    for i in range(10000):
        if i%1000 == 0:
            print(PHOTO_INPUT.active_state())
        time.sleep(1)



def check_pins():
    for i in range(26):
        print(f"Pin {i} set to HIGH")
        input("Press ENTER to increment..\n")
        GPIO.output(i, GPIO.LOW)
    print("Finished checking pins!")

def main():
    monitor_photoresistor()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
