"""
End to end test to check that Raspberry GPIO is properly interfaced
"""

import RPi.GPIO as GPIO

def check_pins():
    i = 0
    while(True):
        input("Press ENTER to increment... Starting at 0")
        i += 1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
        print(f"Pin {i} set to HIGH")
        if i == 25:
            break
    print("Finished checking pins!")


def main():
    check_pins()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
