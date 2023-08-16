import logging

try:
    import RPi.gpio as GPIO
except:
    logging.warning("Failed to import RPi.GPIO")
